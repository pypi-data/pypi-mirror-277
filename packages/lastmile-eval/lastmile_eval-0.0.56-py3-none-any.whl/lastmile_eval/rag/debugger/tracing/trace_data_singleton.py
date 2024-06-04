import json
import logging
import mimetypes
import os
from copy import deepcopy
from datetime import datetime
from enum import Enum
from random import randint
from typing import Any, Optional, get_args

import requests
from requests import Response

# from lastmile_eval.rag.debugger.api import RAGIngestionEvent
from lastmile_eval.rag.debugger.common.query_trace_types import RAGQueryEvent
from lastmile_eval.rag.debugger.common.ingestion_trace_types import (
    RAGIngestionEvent,
)


from ..common.core import (
    IndexingTraceID,
    ParamInfoKey,
    RagQueryEventName,
    RAGTraceType,
)
from ..common.utils import SHOW_DEBUG, Singleton, raise_for_status

ALLOWED_RAG_QUERY_EVENTS = get_args(RagQueryEventName)


class TraceDataSingleton(Singleton):
    """
    Singleton object to store trace-level data. By delegating the state
    management to this class, we also ensure that it is not out of sync
    when shared across multiple classes.

    For example, this is used to reference the same data in
    LastMileOTLSpanExporter, LastMileTracer, and the SDK util files
    """

    _is_already_initialized = False

    def __init__(self, global_params: Optional[dict[str, Any]] = None):
        if self._is_already_initialized:
            return

        super().__init__()

        # This connects to dict global_params, which will get updated whenever trace is not defined (which is what we want)
        if global_params is not None:
            self.global_params = {
                ParamInfoKey(k): v for (k, v) in global_params.items()
            }
        else:
            self.global_params = {}

        self.trace_specific_params = deepcopy(self.global_params)

        # TODO: Have explicit typing for rag_events, which is used for
        # add_rag_query_event and add_rag_ingestion_event
        # Rag_events stores "events" and "indexing_trace_id" fields
        self.rag_events: dict[str, dict[str, Any]] = {}
        # TODO: Change type from dict to class with explicit field and schema
        self.rag_event_sequence: list[dict[str, Any]] = []
        self._added_spans: set[str] = set()
        self._rag_event_for_trace: Optional[dict[str, Any]] = None

        self._rag_trace_type: Optional[RAGTraceType] = None

        # To populate later when we first create a span using one of
        # these two methods:
        #   1) `lastmile_tracer.start_as_current_span()`
        #   2) `lastmile_tracer.start_span()`
        # See opentelemetry.sdk.trace for their SDK API
        self._trace_id: Optional[str] = None

        self.logger_filepaths: set[str] = set()

        self._is_already_initialized = True
        self.project_id: Optional[str] = None
        self.previous_trace_id: Optional[str] = None

        self._span_count: int = 0

    # TODO: Centralize this with `add_rag_query_event` once we
    # have defined ingestion events and can share nearly all logic
    def add_rag_ingestion_event(self, _event: RAGIngestionEvent) -> None:
        """
        Add RagIngestionEvent to the trace-level data
        """
        if self._rag_trace_type == "Query":
            raise ValueError(
                "You have already marked a RAGQueryEvent in this trace. Please check for other calls to `mark_rag_query_trace_event()` within the same trace and either remove them, or do not implement `mark_rag_ingestion_trace_event()`"
            )
        if self.trace_id is None:
            raise ValueError(
                "You must be inside of a trace in order to log a RagQueryEvent"
            )

        # TODO: Add event validation checks once we have ingestion event types
        # event_class_name = type(event).__name__
        event_class_name = "MockIngestionEventPerformed"
        # if event_class_name not in ALLOWED_RAG_QUERY_EVENTS:
        #     raise ValueError(
        #         f"You must log a defined RagQueryEvent type. You are trying to log '{event_class_name}'. Acceptable event types are: {ALLOWED_RAG_QUERY_EVENTS}"
        #     )

        if event_class_name in self.rag_events:
            # TODO: store where stack trace was called from
            raise ValueError(
                f"You have already added an event of type {event_class_name} to add_rag_ingestion_event in this trace. You can only declare this event once per trace. Alternatively, you can use `add_rag_event_for_span` to create multiple events of the same event type, with each event tied to a separate span"
            )
        # TODO: Use .model_dump_json() once we have ingestion events
        # event_json = event.model_dump_json()
        event_json = json.dumps({"data": "Mock ingestion event data"})
        self.rag_events[event_class_name] = {"event": event_json}
        self._rag_trace_type = "Ingestion"

    def add_rag_query_event(
        self,
        event: RAGQueryEvent,
        indexing_trace_id: Optional[IndexingTraceID] = None,
    ) -> None:
        """
        Add RagQueryEvent to the trace-level data
        """
        # TODO: Implement Enum instead of string literal
        if self._rag_trace_type == "Ingestion":
            raise ValueError(
                "You have already marked a RAGIngestionEvent in this trace. Please check for other calls to `mark_rag_ingestion_trace_event()` within the same trace and either remove them, or do not implement `mark_rag_query_trace_event()`"
            )

        if self.trace_id is None:
            raise ValueError(
                "You must be inside of a trace in order to log a RagQueryEvent"
            )

        event_class_name = type(event).__name__
        if event_class_name not in ALLOWED_RAG_QUERY_EVENTS:
            raise ValueError(
                f"You must log a defined RagQueryEvent type. You are trying to log '{event_class_name}'. Acceptable event types are: {ALLOWED_RAG_QUERY_EVENTS}"
            )
        if event_class_name in self.rag_events:
            # TODO: store where stack trace was called from
            raise ValueError(
                f"You have already added an event of type {event_class_name} to add_rag_query_event in this trace. You can only declare this event once per trace. Alternatively, you can use `add_rag_event_for_span` to create multiple events of the same event type, with each event tied to a separate span"
            )
        event_json = event.model_dump_json()
        self.rag_events[event_class_name] = {
            "event": event_json,
            # TODO: Check other events if indexing_trace_ids are mismatched and flag if they are
            "indexing_trace_id": indexing_trace_id,
        }
        self._rag_trace_type = "Query"

    def add_rag_event_for_span(
        self,
        # TODO: Explicit schema for event_payload
        event_payload: dict[str, Any],
    ) -> None:
        """
        Add RagEvent to the trace-level data. Duplicate from
        add_rag_query_event for now just to get unblocked
        """
        span_id = event_payload.get("span_id")
        if span_id is None:
            raise ValueError("Could not extract span_id from event payload")
        if span_id in self._added_spans:
            raise ValueError(
                f"You have already added an event for span id '{span_id}'. Please check for other calls to `add_rag_event_for_span()` within the same span and either remove them, or explicitly pass the `span_id` argument in `add_rag_event_for_span()`."
            )
        if self.trace_id is None:
            raise ValueError(
                "Unable to detect current trace_id. You must be inside of a trace in order to log a RagEvent"
            )

        self._added_spans.add(span_id)
        self.rag_event_sequence.append(event_payload)

    def add_rag_event_for_trace(
        self,
        # TODO: Explicit schema for event_payload
        event_payload: dict[str, Any],
    ) -> None:
        """
        Add RagEvent to the trace-level data. Same functionality as
        `add_rag_event_for_span` except this is used for the overall
        trace-level data instead of at the span level.
        """
        if self.trace_id is None:
            raise ValueError(
                "Unable to detect current trace_id. You must be inside of a trace in order to log a RagEvent"
            )
        if self._rag_event_for_trace is not None:
            raise ValueError(
                f"You have already added an event for trace id '{self.trace_id}'. Please check for other calls to `add_rag_event_for_trace()` within the same trace."
            )
        self._rag_event_for_trace = event_payload

    def get_params(self) -> dict[str, Any]:
        """
        Get the parameters saved in the trace-level data (which is the same as
        global if no trace exists)
        """
        return {str(k): v for (k, v) in self.trace_specific_params.items()}

    def register_param(self, key: str, value: Any) -> None:
        """
        Register a parameter to the trace-level data (and global params if no
        trace is defined). If the key is already defined, create a new key
        which is "key-1", "key-2", etc.
        """
        # Use string literals instead of enums because if we have the same key
        # we want to be able to differentiate them more easily
        # (ex: "chunks" vs. "chunks-1") instead of comparing enums
        # (ex: "EventPayload.CHUNKS" vs. "chunks-1")
        if isinstance(key, Enum):
            key = key.value

        param_key = ParamInfoKey(key)
        should_write_to_global = False
        if self.trace_id is None:
            should_write_to_global = True

        # Even if trace_id is None (not in a trace), we still need to update
        # trace_specific_params so it's not out of sync with global_params

        # For auto-instrumentation, we have tons of events with the same
        # event_name so adding more specific parameters there
        if param_key in self.trace_specific_params:
            i = 1
            while param_key + "-" + str(i) in self.trace_specific_params:
                i += 1
            param_key = ParamInfoKey(param_key + "-" + str(i))
        self.trace_specific_params[param_key] = value

        if should_write_to_global:
            param_key = ParamInfoKey(key)
            if param_key in self.global_params:
                i = 1
                while param_key + "-" + str(i) in self.global_params:
                    i += 1
                param_key = ParamInfoKey(param_key + "-" + str(i))
            self.global_params[param_key] = value

    def clear_params(
        self,
        should_clear_global_params: bool = False,
    ) -> None:
        """
        Clear the parameters saved in the trace-level data, as well as
        global params if `should_clear_global_params` is true.
        """
        self.trace_specific_params.clear()
        if should_clear_global_params:
            self.global_params.clear()

    def log_to_rag_traces_table(self, lastmile_api_token: str) -> Response:
        """
        Log the trace-level data to the RagIngestionTraces or RagQueryTraces
        table via the respective LastMile endpoints. This logs data that
        was added to the singleton via one of these methods:
            1. `add_rag_query_event`
            2. `add_rag_ingestion_event`
            3. `add_rag_event_for_trace`

        @param lastmile_api_token (str): Used for authentication.
            Create one from the "API Tokens" section from this website:
            https://lastmileai.dev/settings?page=tokens

        @return Response: The response from the LastMile endpoint
        """
        if self.trace_id is None:
            raise ValueError(
                "Unable to detect trace id. Please create a root span using `tracer.start_as_current_span()`"
            )

        payload: dict[str, Any] = {
            "traceId": self.trace_id,
            "paramSet": self.get_params(),
        }
        if self.project_id is not None:
            payload["projectId"] = self.project_id

        # Process the trace-level data from `add_rag_event_for_trace()`
        payload_event_data: dict[Any, Any] = {}
        if self._rag_event_for_trace is not None:
            event_input = self._rag_event_for_trace.get("input")
            if event_input is not None:
                payload["input"] = event_input

            event_output = self._rag_event_for_trace.get("output")
            if event_output is not None:
                payload["output"] = self._rag_event_for_trace.get("output")

            event_data_from_trace = self._rag_event_for_trace.get("event_data")
            if event_data_from_trace is not None:
                payload_event_data.update(event_data_from_trace)

            indexing_trace_id = self._rag_event_for_trace.get(
                "indexing_trace_id"
            )
            if indexing_trace_id is not None:
                payload["ragIngestionTraceId"] = indexing_trace_id

        if self._rag_trace_type == "Ingestion":
            payload.update(
                {
                    "eventData": payload_event_data,
                    # TODO: Add fields below
                    # metadata
                    # orgId
                    # visibility
                }
            )
            if SHOW_DEBUG:
                print(f"TraceDataSingleton.log_to_traces_table: {payload=}")

            response = requests.post(
                "https://lastmileai.dev/api/rag_ingestion_traces/create",
                headers={"Authorization": f"Bearer {lastmile_api_token}"},
                json=payload,
                timeout=60,  # TODO: Remove hardcoding
            )
            raise_for_status(
                response,
                "Error creating rag ingestion trace",
            )
            return response

        # Default to RAGQueryTraces if RagEventType is unspecified
        indexing_trace_id = None
        query = self._get_rag_query_event("QueryReceived")
        if query is not None:
            payload_event_data["QueryReceived"] = json.loads(query["event"])
            if "indexing_trace_id" in query:
                indexing_trace_id = query["indexing_trace_id"]

        context_retrieved = self._get_rag_query_event("ContextRetrieved")
        if context_retrieved is not None:
            payload_event_data["ContextRetrieved"] = json.loads(
                context_retrieved["event"]
            )
            if "indexing_trace_id" in context_retrieved:
                indexing_trace_id = context_retrieved["indexing_trace_id"]

        fully_resolved_prompt = self._get_rag_query_event("PromptResolved")
        if fully_resolved_prompt is not None:
            payload_event_data["PromptResolved"] = json.loads(
                fully_resolved_prompt["event"]
            )
            if "indexing_trace_id" in fully_resolved_prompt:
                indexing_trace_id = fully_resolved_prompt["indexing_trace_id"]

        llm_output_received = self._get_rag_query_event("LLMOutputReceived")
        if llm_output_received is not None:
            payload_event_data["LLMOutputReceived"] = json.loads(
                llm_output_received["event"]
            )
            if "indexing_trace_id" in llm_output_received:
                indexing_trace_id = llm_output_received["indexing_trace_id"]

        payload.update(
            {
                # structured data required for RagQueryTrace DB
                "query": query or {},
                "context": context_retrieved or {},
                "fullyResolvedPrompt": fully_resolved_prompt or {},
                "llmOutput": llm_output_received or {},
                # unstructured data for RagEvent info
                "eventData": payload_event_data,
                # TODO: Add fields below
                # metadata
                # orgId
                # visibility
            }
        )

        if indexing_trace_id is not None:
            payload["ragIngestionTraceId"] = str(indexing_trace_id)
        if SHOW_DEBUG:
            print(f"TraceDataSingleton.log_to_rag_traces_table {payload=}")

        response: Response = requests.post(
            "https://lastmileai.dev/api/rag_query_traces/create",
            headers={"Authorization": f"Bearer {lastmile_api_token}"},
            json=payload,
            timeout=60,  # TODO: Remove hardcoding
        )
        raise_for_status(
            response,
            "Error creating rag query trace",
        )
        return response

    def log_span_rag_events(self, lastmile_api_token: str) -> None:
        if not self.rag_event_sequence:
            return

        if self.trace_id is None:
            raise ValueError(
                "Unable to detect trace id. Please create a root span using `tracer.start_as_current_span()`"
            )

        for event_payload in self.rag_event_sequence:
            # TODO: Schematize event data payload
            payload: dict[str, Any] = {
                # Required fields by user (or auto-instrumentation)
                "eventName": event_payload["event_name"] or "",
                "input": event_payload["input"] or {},
                "output": event_payload["output"] or {},
                "eventData": event_payload["event_data"] or {},
                "metadata": {} or "",  # TODO: Allow user to define metadata
                # Required but get this from our data when marking event
                "traceId": self.trace_id,
                "spanId": event_payload["span_id"],
                # TODO: Add fields below
                # orgId
                # visibility
            }
            if self.project_id is not None:
                payload["projectId"] = self.project_id
            indexing_trace_id = event_payload.get("indexing_trace_id")
            if indexing_trace_id is not None:
                payload["ragIngestionTraceId"] = indexing_trace_id
            if SHOW_DEBUG:
                print(f"TraceDataSingleton.log_span_rag_events: {payload=}")

            response = requests.post(
                "https://lastmileai.dev/api/rag_events/create",
                headers={"Authorization": f"Bearer {lastmile_api_token}"},
                json=payload,
                timeout=60,  # TODO: Remove hardcoding
            )
            raise_for_status(
                response,
                "Error creating rag event",
            )
        return None

    def log_data(self, data: Any, logger: logging.Logger) -> None:
        """
        Log the data, save it to a file (if it doesn't exist) so that we can
        export it later
        """
        # TODO: Allow user to specify logger level instead of just info
        logger.info(repr(data))

        # TODO: Cache handlers so we don't have to check every time
        for handler in logger.handlers:
            if isinstance(handler, logging.FileHandler):
                filepath = handler.baseFilename
                self.logger_filepaths.add(filepath)
            else:
                # TODO: If file handler is not present, then create one
                # based on logger name and add it to logger
                # handler.get_name()
                pass

    def upload_log_data(self, lastmile_api_token: str) -> None:
        """
        1. Get all the data from logger files, run foreach on all
        2. S3 bucket upload file
        3. api/upload/create --> get upload Id
        4. evaluation_trace_log/create
        """
        for filepath in self.logger_filepaths:
            if SHOW_DEBUG:
                print(f"Uploading {filepath} log data to LastMile...")

            # Upload log file to S3
            s3_upload_obj = _upload_to_s3(filepath, lastmile_api_token)
            if s3_upload_obj is None:
                # TODO: Add true error handling to logger files
                print(f"Error: Failed to upload logger file {filepath} to S3")
                continue

            # Create upload object to LastMile DB
            upload_response = requests.post(
                "https://lastmileai.dev/api/upload/create",
                headers={"Authorization": f"Bearer {lastmile_api_token}"},
                json={
                    "url": s3_upload_obj["url"],
                    "metadata": s3_upload_obj["metadata"],
                },
                timeout=60,  # TODO: Remove hardcoding
            )
            raise_for_status(
                upload_response,
                f"Error creating upload object with S3 url {s3_upload_obj['url']}",
            )

            # Create evaluation trace log to LastMile DB
            upload_id = upload_response.json()["id"]
            payload = {"traceId": self.trace_id, "uploadId": upload_id}
            if self.project_id is not None:
                payload["projectId"] = self.project_id
            log_response = requests.post(
                "https://lastmileai.dev/api/evaluation_trace_log/create",
                headers={"Authorization": f"Bearer {lastmile_api_token}"},
                json=payload,
                timeout=60,  # TODO: Remove hardcoding
            )
            raise_for_status(
                log_response,
                f"Error creating evaluation trace log with payload: {payload}",
            )

    def reset(self) -> None:
        """
        Reset the trace-level data
        """
        # allows capture trace id after trace is completed.
        self.previous_trace_id = None
        self.previous_trace_id = self.trace_id

        self.trace_specific_params = deepcopy(self.global_params)
        self.trace_id = None
        self.rag_events.clear()
        self.rag_event_sequence = []
        self._added_spans.clear()
        self._rag_trace_type = None
        self._rag_event_for_trace = None
        self.span_count = 0

        # TODO: Clear log files themselves too
        self.logger_filepaths.clear()

    @property
    def trace_id(  # pylint: disable=missing-function-docstring
        self,
    ) -> Optional[str]:
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value: Optional[str]) -> None:
        self._trace_id = value

    @property
    def span_count(  # pylint: disable=missing-function-docstring
        self,
    ) -> int:
        return self._span_count

    @span_count.setter
    def span_count(self, value: int) -> None:
        self._span_count = value

    def _get_rag_query_event(
        self, event_class_name: str
    ) -> Optional[dict[str, Any]]:
        """
        Get the JSON string representation of the RagQueryEvent (and index
        trace id if it exists) for a given RagQueryEventName.

        If RagQueryEventName is not registered in the rag_query_events, we
        return None
        """
        if event_class_name not in ALLOWED_RAG_QUERY_EVENTS:
            raise ValueError(
                f"Unable to detect RAGQueryEvent from '{event_class_name}'. Acceptable event types are: {ALLOWED_RAG_QUERY_EVENTS}"
            )
        return self.rag_events.get(event_class_name)


def _upload_to_s3(
    filepath: str, lastmile_api_token: str
) -> Optional[
    dict[str, Any]  # TODO: Schematize return type for s3_upload_object
]:
    """
    Upload the logger file to S3 and return the URL

    @return S3 upload object if successful, None if not
        s3_upload_object = { "url": string, "metadata": dict }
    """
    policy_response = requests.get(
        "https://lastmileai.dev/api/upload/policy",
        headers={
            "content-type": "application/json",
            "Authorization": "Bearer " + lastmile_api_token,
        },
        timeout=60,  # TODO: Remove hardcoding
    )
    raise_for_status(
        policy_response,
        "Error getting upload policy to load file to S3 bucket",
    )

    url = "https://s3.amazonaws.com/files.uploads.lastmileai.com"
    policy = policy_response.json()
    date_string = _get_date_time_string()
    filename: str = _sanitize_filename(os.path.basename(filepath))
    random_int: int = randint(0, 10001)
    upload_key: str = (
        f"uploads/{policy['userId']}/{date_string}/{random_int}/{filename}"
    )

    mime_type = mimetypes.guess_type(filepath)[0]
    form_data = {
        "key": upload_key,
        "acl": "public-read",
        "Content-Type": mime_type,
        "AWSAccessKeyId": policy["AWSAccessKeyId"],
        "success_action_status": "201",
        "Policy": policy["s3Policy"],
        "Signature": policy["s3Signature"],
        "file": open(filepath, "rb"),
    }

    s3_upload_response = requests.post(
        "https://s3.amazonaws.com/files.uploads.lastmileai.com",
        files=form_data,
        timeout=60,  # TODO: Remove hardcoding
    )
    s3_url = f"{url}/{upload_key}"
    raise_for_status(
        s3_upload_response,
        f"Error uploading file to S3 url {s3_url}",
    )

    return {
        "url": s3_url,
        "metadata": {
            "size": os.path.getsize(filepath),
            "title": filename,
            "type": mime_type,
        },
    }


def _sanitize_filename(filename: str) -> str:
    """
    Sanitize the filename to remove any characters that are not allowed in
    S3 filenames
    """
    return filename.replace("+", "_")


def _get_date_time_string() -> str:
    now = datetime.now()
    return now.strftime("%Y_%m_%d_%H_%M_%S")
