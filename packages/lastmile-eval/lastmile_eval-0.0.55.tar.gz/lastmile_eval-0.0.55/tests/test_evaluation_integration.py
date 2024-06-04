"""
TODO: mock out the web endpoint so key is not needed to test.
"""

import json
import logging
import os
from typing import Optional

import lastmile_utils.lib.core.api as core_utils
import pandas as pd
from dotenv import load_dotenv

from lastmile_eval.rag.debugger import evaluation_lib as e_lib
from lastmile_eval.rag.debugger.api import evaluation as e
from lastmile_eval.rag.debugger.common import core as core

TEST_WEBSITE_BASE_URL = "https://lastmileai.dev"
N_DEFAULT_AGGREGATES = 3
N_EXPECTED_COLUMNS_EVALS_TRACE = 4
N_EXPECTED_COLUMNS_EVALS_DATASET = 3

logger = logging.getLogger(__name__)
logging.basicConfig(format=core_utils.LOGGER_FMT, level=logging.INFO)


load_dotenv(override=True)
token = os.getenv("LASTMILE_API_TOKEN")
assert token is not None, "Token not found"


def pdoptions(
    r: Optional[int] = 2,
    c: Optional[int] = 20,
    w: Optional[int] = 50,
    dw: Optional[int] = 50,
):
    pd.set_option("display.max_rows", r)
    pd.set_option("display.max_columns", c)
    pd.set_option("display.max_colwidth", w)
    pd.set_option("display.width", dw)


# Just for manual testing.
def _lookup_example_set_ids_by_name(name: str) -> list[core.ExampleSetID]:  # type: ignore
    return e_lib._get_example_set_ids_by_name(  # type: ignore
        core.BaseURL(TEST_WEBSITE_BASE_URL),
        name,
        os.getenv("LASTMILE_API_TOKEN"),  # type: ignore
    ).unwrap_or_raise(ValueError)


def assert_evaluation_values(
    resp: e_lib.CreateEvaluationResponse,
    example_level_records: Optional[list[tuple[str, float | str]]] = None,
    aggregated_records: Optional[list[tuple[str, float | str]]] = None,
):
    df_metrics_aggregated = resp.df_metrics_aggregated
    assert len(set(df_metrics_aggregated.exampleSetId)) == 1  # type: ignore

    if example_level_records is not None:
        trace_metrics = resp.df_metrics_example_level[["metricName", "value"]].fillna("None").to_records(index=False).tolist()  # type: ignore

        # TODO: this should be a bag check, not set
        assert set(trace_metrics) == set(example_level_records)  # type: ignore

    if aggregated_records is not None:
        df_metrics_aggregated = resp.df_metrics_aggregated
        dataset_metrics = df_metrics_aggregated[["metricName", "value"]].fillna("None").to_records(index=False).tolist()  # type: ignore

        # TODO: this should be a bag check, not set
        assert set(dataset_metrics) == set(aggregated_records)  # type: ignore


def assert_example_set_create_response(
    resp: e_lib.CreateExampleSetResponse | e_lib.CreateQuerySetResponse,
    name: str,
    message_values_present: Optional[set[str]] = None,
):
    message_values_present = message_values_present or set()

    assert resp.success

    msg_obj = json.loads(resp.message)
    assert msg_obj.keys() == {
        "id",
        "createdAt",
        "updatedAt",
        "name",
        "description",
        "creatorId",
        "projectId",
        "organizationId",
        "visibility",
        "active",
        "metadata",
    }

    for k, v in msg_obj.items():
        if k in message_values_present:
            assert v is not None, f"Expected {k} to be present, got None."

    assert msg_obj["name"] == name


def assert_df_conditions(
    df: pd.DataFrame,
    cols_contain: Optional[set[str]] = None,
    rows: Optional[int] = None,
    cols: Optional[int] = None,
    nulls_axis0: Optional[list[int]] = None,
    nulls_axis1: Optional[list[int]] = None,
):
    if cols_contain is not None:
        diff = cols_contain - set(df.columns)
        assert (
            set(df.columns) >= cols_contain
        ), f"Missing columns: {diff}, Existing columns: {set(df.columns)}"
    if rows is not None:
        assert df.shape[0] == rows

    if cols is not None:
        assert df.shape[1] == cols

    if nulls_axis0 is not None:
        got_nulls_0 = df.isnull().astype(int).sum(axis=0).tolist()  # type: ignore[pandas]
        assert (
            got_nulls_0 == nulls_axis0
        ), f"Expected nulls_axis0: {nulls_axis0}, got {got_nulls_0}"
    if nulls_axis1 is not None:
        got_nulls1 = df.isnull().astype(int).sum(axis=1).tolist()  # type: ignore[pandas]
        assert (
            got_nulls1 == nulls_axis1
        ), f"Expected nulls_axis1: {nulls_axis1}, got {got_nulls1}"


def _assert_evaluation_response_helper(
    resp: e_lib.CreateEvaluationResponse,
    df_trace_shape: tuple[int, int],
    df_dataset_shape: tuple[int, int],
):
    assert isinstance(resp.evaluation_result_id, str)
    assert isinstance(resp.example_set_id, str)
    assert resp.success

    # (0 rows expected) == (df is None)
    assert (df_trace_shape[0] == 0) == (
        resp.df_metrics_example_level is None
    ), f"{df_trace_shape=}, {resp.df_metrics_example_level=}"

    # (1 or more rows expected) -> (df is not None and rows eq)
    # (df is not None and rows eq) or (0 rows expected)
    assert (
        resp.df_metrics_example_level is not None
        and df_trace_shape == resp.df_metrics_example_level.shape
    ) or (
        df_trace_shape[0] == 0
    ), f"{df_trace_shape=}, {resp.df_metrics_example_level=}"

    assert (
        resp.df_metrics_aggregated is not None
        and df_dataset_shape == resp.df_metrics_aggregated.shape
    ) or (
        df_dataset_shape[0] == 0
    ), f"{df_dataset_shape=}, {resp.df_metrics_aggregated=}"


def assert_evaluation_response(
    resp: e_lib.CreateEvaluationResponse,
    n_inputs: int,
    n_evaluators: int,
    n_datasets: int = 1,
    n_trials: int = 1,
    expected_columns_evals_trace: int = N_EXPECTED_COLUMNS_EVALS_TRACE,
    expected_columns_evals_dataset: int = N_EXPECTED_COLUMNS_EVALS_DATASET,
    n_aggregated_evaluators: Optional[int] = None,
):
    n_aggregated_evaluators = (
        n_aggregated_evaluators or n_evaluators * N_DEFAULT_AGGREGATES
    )
    _assert_evaluation_response_helper(
        resp,
        (n_trials * n_inputs * n_evaluators, expected_columns_evals_trace),
        (n_datasets * n_aggregated_evaluators, expected_columns_evals_dataset),
    )


def test_run_and_evaluate_with_in_memory_input_user_provided_trace_ids():
    def run_fn(query: str) -> e.QueryFlowOutput:
        ids = {
            "Is it healthy to stare at the sun?": "clw15xylx003uquta459g4c05"
        }
        outputs = {
            "Is it healthy to stare at the sun?": "This is some arbitrary output",
        }
        return (outputs[query], ids[query])

    queries = ["Is it healthy to stare at the sun?"]

    evaluators = {"exact_match"}

    resp = e.run_and_evaluate(
        project_id=None,
        run_query_fn=run_fn,
        inputs=queries,
        evaluators=evaluators,
        save_options=e.SaveOptions(
            example_set_name="Example set test31.1",
            evaluation_result_name="Evaluation result test31.1",
        ),
    )

    assert_evaluation_response(resp, len(queries), len(evaluators))
    assert_evaluation_values(
        resp,
        [("exact_match", 0.0)],
        [
            ("exact_match_mean", 0.0),
            ("exact_match_std", "None"),
            ("exact_match_count", 1.0),
        ],
    )


def test_evaluate_with_traces_general_case():
    pdoptions(r=None, c=None, dw=None)

    def _download_traces():
        for df in e.download_query_traces(
            project_id=None,
            batch_limit=2,
        ):
            return df

        raise ValueError("No data found")

    def _clean_trace_df(df_traces: pd.DataFrame) -> pd.DataFrame:
        cols_keep = [
            "ragQueryTraceId",
            "traceId",
            "ragIngestionTrace",
        ]

        df_traces = df_traces[cols_keep]  # type: ignore[fixme]
        df_traces["input"] = [f"The input {i}" for i in range(len(df_traces))]  # type: ignore[fixme]
        df_traces["output"] = [f"The output {i}" for i in range(len(df_traces))]  # type: ignore[fixme]

        return df_traces

    df_traces = _clean_trace_df(_download_traces())

    evaluators = {"exact_match"}

    resp = e.evaluate(
        project_id=None,
        examples_dataframe=df_traces,
        evaluators=e.get_default_evaluators(evaluators),
        save_options=e.SaveOptions(
            example_set_name="Example set test30.1",
            evaluation_result_name="Evaluation result test30.1",
        ),
    )

    assert_evaluation_response(resp, len(df_traces), len(evaluators))
    assert_evaluation_values(
        resp,
        [("exact_match", 0.0), ("exact_match", 0.0)],
        [
            ("exact_match_mean", 0.0),
            ("exact_match_std", 0.0),
            ("exact_match_count", 2.0),
        ],
    )


def test_evaluation_save_options_combinations():
    evaluators = {"exact_match"}

    queries = ["x", "y"]
    resp = e.evaluate(
        project_id=None,
        examples_dataframe=pd.DataFrame(
            {
                "query": queries,
                "groundTruth": [
                    "xgt",
                    "ygt",
                ],
            }
        ),
        evaluators=evaluators,
        save_options=e.SaveOptions(
            example_set_name="Example set test29.1",
            evaluation_result_name="Evaluation result test29.1",
        ),
    )

    assert_evaluation_response(resp, len(queries), len(evaluators))
    assert_evaluation_values(
        resp,
        [("exact_match", 0.0), ("exact_match", 0.0)],
        [
            ("exact_match_mean", 0.0),
            ("exact_match_std", 0.0),
            ("exact_match_count", 2.0),
        ],
    )

    def run_fn(query: str) -> str:
        return f"This is the output. The query was: {query}"

    queries = [
        "x",
        "y",
    ]

    resp = e.run_and_evaluate(
        project_id=None,
        run_query_fn=run_fn,
        inputs=queries,
        ground_truths=[
            "xgt",
            "ygt",
        ],
        evaluators=evaluators,
        save_options=e.SaveOptions(
            example_set_name="Example set test29.1",
            evaluation_result_name="Evaluation result test29.1",
        ),
    )

    assert_evaluation_response(resp, len(queries), len(evaluators))
    assert_evaluation_values(
        resp,
        [("exact_match", 0.0), ("exact_match", 0.0)],
        [
            ("exact_match_mean", 0.0),
            ("exact_match_std", 0.0),
            ("exact_match_count", 2.0),
        ],
    )

    queries = [
        "x",
        "y",
    ]

    resp = e.evaluate(
        project_id=None,
        examples_dataframe=pd.DataFrame(
            {
                "query": queries,
                "groundTruth": [
                    "xgt",
                    "ygt",
                ],
            }
        ),
        evaluators=evaluators,
        save_options=e.SaveOptions(
            evaluation_result_name="Evaluation result test29.2",
        ),
    )

    assert_evaluation_response(resp, len(queries), len(evaluators))

    assert_evaluation_values(
        resp,
        [("exact_match", 0.0), ("exact_match", 0.0)],
        [
            ("exact_match_mean", 0.0),
            ("exact_match_std", 0.0),
            ("exact_match_count", 2.0),
        ],
    )

    queries = [
        "x",
        "y",
    ]

    resp = e.run_and_evaluate(
        project_id=None,
        run_query_fn=run_fn,
        inputs=queries,
        ground_truths=[
            "xgt",
            "ygt",
        ],
        evaluators=evaluators,
        save_options=e.SaveOptions(
            example_set_name="Example set test29.3",
        ),
    )

    assert_evaluation_response(resp, len(queries), len(evaluators))
    assert_evaluation_values(
        resp,
        [("exact_match", 0.0), ("exact_match", 0.0)],
        [
            ("exact_match_mean", 0.0),
            ("exact_match_std", 0.0),
            ("exact_match_count", 2.0),
        ],
    )


def test_run_and_evaluate_general_case_with_default_evaluators():
    def run_fn(query: str) -> str:
        return f"This is the output. The query was: {query}"

    evaluators = {
        # unary
        "toxicity",
        "sentiment",
        # binary - GT
        "bleu",
        "rouge1",
        "similarity",
        "exact_match",
        # binary - input
        "relevance",
        # ternary
        "qa",
        "human_vs_ai",
    }

    queries = ["x", "z"]

    resp = e.run_and_evaluate(
        project_id=None,
        run_query_fn=run_fn,
        inputs=queries,
        ground_truths=["x", "W"],
        evaluators=evaluators,
    )

    assert_evaluation_response(resp, len(queries), len(evaluators))

    trace_metrics_names = resp.df_metrics_example_level[["metricName"]].fillna("None").to_records(index=False).tolist()  # type: ignore

    # TODO: this should be a bag check, not set
    assert set(trace_metrics_names) == {  # type: ignore
        ("relevance",),
        ("relevance",),
        ("sentiment",),
        ("sentiment",),
        ("exact_match",),
        ("exact_match",),
        ("bleu",),
        ("bleu",),
        ("toxicity",),
        ("toxicity",),
        ("similarity",),
        ("similarity",),
        ("rouge1",),
        ("rouge1",),
        ("human_vs_ai",),
        ("human_vs_ai",),
        ("qa",),
        ("qa",),
    }
    trace_metrics_values = resp.df_metrics_example_level["value"]  # type: ignore[pandas]
    assert ((0 <= trace_metrics_values) & (trace_metrics_values <= float("inf"))).all(), f"{trace_metrics_values=}"  # type: ignore[pandas]

    df_metrics_aggregated = resp.df_metrics_aggregated

    assert len(set(df_metrics_aggregated.exampleSetId)) == 1  # type: ignore
    dataset_metrics_names = df_metrics_aggregated[["metricName"]].fillna("None").to_records(index=False).tolist()  # type: ignore

    # TODO: this should be a bag check, not set
    assert set(dataset_metrics_names) == {  # type: ignore
        ("human_vs_ai_count",),
        ("relevance_std",),
        ("sentiment_mean",),
        ("human_vs_ai_std",),
        ("qa_count",),
        ("qa_std",),
        ("sentiment_std",),
        ("bleu_count",),
        ("toxicity_mean",),
        ("qa_mean",),
        ("exact_match_count",),
        ("toxicity_count",),
        ("bleu_mean",),
        ("rouge1_mean",),
        ("bleu_std",),
        ("rouge1_std",),
        ("exact_match_std",),
        ("relevance_mean",),
        ("relevance_count",),
        ("similarity_mean",),
        ("exact_match_mean",),
        ("rouge1_count",),
        ("similarity_count",),
        ("sentiment_count",),
        ("toxicity_std",),
        ("similarity_std",),
        ("human_vs_ai_mean",),
    }

    df_metrics_aggregated = resp.df_metrics_aggregated
    dataset_metrics_values = df_metrics_aggregated["value"]  # type: ignore[pandas]
    assert ((0 <= dataset_metrics_values) & (dataset_metrics_values <= float("inf"))).all(), f"{dataset_metrics_values=}"  # type: ignore[pandas]


def test_run_and_evaluate_bad_no_evaluators():
    def run_fn(query: str) -> str:
        return f"This is the output. The query was: {query}"

    try:
        resp = e.run_and_evaluate(
            project_id=None,
            run_query_fn=run_fn,
            input_set_id="clwoenwjo0039qymx70nk09k6",
            n_trials=2,
        )

        assert False, f"Expected ValueError, got {resp}"
    except ValueError as exn:
        expected = "No evaluators provided or inferred. Please provide at least one evaluator"
        assert expected in str(exn), f"{str(exn)=}"


def test_run_and_evaluate_2_trials():
    def run_fn(query: str) -> str:
        return f"This is the output. The query was: {query}"

    evaluators = {"exact_match"}

    resp = e.run_and_evaluate(
        project_id=None,
        run_query_fn=run_fn,
        input_set_id="clwoenwjo0039qymx70nk09k6",
        evaluators=evaluators,
        n_trials=2,
    )
    assert_evaluation_response(resp, 2, len(evaluators), n_trials=2)

    assert_evaluation_values(
        resp,
        [("exact_match", 0.0), ("exact_match", 0.0)],
        [
            ("exact_match_mean", 0.0),
            ("exact_match_count", 4.0),
            ("exact_match_std", 0.0),
        ],
    )


def test_run_and_evaluate_with_input_set_id():
    def run_fn(query: str) -> str:
        return f"This is the output. The query was: {query}"

    evaluators = {"exact_match"}

    resp = e.run_and_evaluate(
        project_id=None,
        run_query_fn=run_fn,
        input_set_id="clwoenwjo0039qymx70nk09k6",
        evaluators=evaluators,
    )

    assert_evaluation_response(resp, 2, len(evaluators))

    assert_evaluation_values(
        resp,
        [("exact_match", 0.0), ("exact_match", 0.0)],
        [
            ("exact_match_mean", 0.0),
            ("exact_match_std", 0.0),
            ("exact_match_count", 2.0),
        ],
    )


def test_run_and_evaluate_with_in_memory_inputs():
    def run_fn(query: str) -> str:
        return f"This is the output. The query was: {query}"

    evaluators = {"exact_match"}

    resp = e.run_and_evaluate(
        project_id=None,
        run_query_fn=run_fn,
        inputs=["x", "y"],
        ground_truths=["xgt", "ygt"],
        evaluators=evaluators,
    )

    assert_evaluation_response(resp, 2, len(evaluators))

    assert_evaluation_values(
        resp,
        [("exact_match", 0.0), ("exact_match", 0.0)],
        [
            ("exact_match_mean", 0.0),
            ("exact_match_std", 0.0),
            ("exact_match_count", 2.0),
        ],
    )


def test_run_and_evaluate_bad_missing_queries():
    def run_fn(query: str) -> str:
        return f"This is the output. The query was: {query}"

    evaluators = {"exact_match"}
    try:
        resp = e.run_and_evaluate(
            project_id=None,
            run_query_fn=run_fn,
            ground_truths=["xgt", "ygt"],
            evaluators=evaluators,
        )

        assert False, f"Expected ValueError, got {resp}"

    except ValueError as exn:
        expected = "ground_truths given but no input queries given"
        assert expected in str(exn), f"{str(exn)=}"


def test_run_and_evaluate_bad_ground_truth_missing_queries():
    def run_fn(query: str) -> str:
        return f"This is the output. The query was: {query}"

    evaluators = {"exact_match"}

    try:
        resp = e.run_and_evaluate(
            project_id=None,
            run_query_fn=run_fn,
            input_set_id="clwoenwjo0039qymx70nk09k6",
            ground_truths=["xgt", "ygt"],
            evaluators=evaluators,
        )

        assert False, f"Expected ValueError, got {resp}"
    except ValueError as exn:
        expected = "ground_truths given but no input queries given"
        assert expected in str(exn), f"{str(exn)=}"


def test_run_and_evaluate_bad_duplicate_args():
    def run_fn(query: str) -> e.QueryFlowOutput:
        return f"This is the output. The query was: {query}"

    evaluators = {"exact_match"}

    try:
        resp = e.run_and_evaluate(
            project_id=None,
            run_query_fn=run_fn,
            input_set_id="clwoenwjo0039qymx70nk09k6",
            inputs=["x", "y"],
            ground_truths=["xgt", "ygt"],
            evaluators=evaluators,
        )

        assert False, f"Expected ValueError, got {resp}"
    except ValueError as exn:
        expected = "Exactly one of (input_set_id, inputs) must be provided."
        assert expected in str(exn), f"{str(exn)=}"


def test_evaluate_with_evaluator_names():
    evaluators = {"exact_match"}

    queries = ["x", "y"]

    resp = e.evaluate(
        project_id=None,
        examples_dataframe=pd.DataFrame(
            {"query": queries, "groundTruth": ["xgt", "ygt"]}
        ),
        evaluators=evaluators,
    )

    assert_evaluation_response(resp, len(queries), len(evaluators))

    assert_evaluation_values(
        resp,
        [("exact_match", 0.0), ("exact_match", 0.0)],
        [
            ("exact_match_mean", 0.0),
            ("exact_match_std", 0.0),
            ("exact_match_count", 2.0),
        ],
    )


def test_evaluate_with_save_options():
    evaluators = {"exact_match"}

    queries = ["x", "y"]

    resp = e.evaluate(
        project_id=None,
        examples_dataframe=pd.DataFrame(
            {"query": queries, "groundTruth": ["xgt", "ygt"]}
        ),
        evaluators=e.get_default_evaluators(evaluators),
        save_options=e.SaveOptions(
            example_set_name="Example set test19",
            evaluation_result_name="Evaluation result test19",
        ),
    )

    assert_evaluation_response(resp, len(queries), len(evaluators))

    assert_evaluation_values(
        resp,
        [("exact_match", 0.0), ("exact_match", 0.0)],
        [
            ("exact_match_mean", 0.0),
            ("exact_match_std", 0.0),
            ("exact_match_count", 2.0),
        ],
    )


def test_evaluate_with_custom_exact_match_agg():
    def my_agg_evaluator(df_example_level_metrics: pd.DataFrame) -> float:
        return (
            df_example_level_metrics.apply(  # type: ignore[pandas]
                lambda r: r["input"] == r["output"],  # type: ignore[pandas]
                axis=1,
            )
            .astype(float)
            .max()
        )

    queries = ["x", "y"]

    aggregated_evaluators = dict(my_agg_v0=my_agg_evaluator)

    resp = e.evaluate(
        project_id=None,
        examples_dataframe=pd.DataFrame(
            {"query": queries, "groundTruth": ["xgt", "ygt"]}
        ),
        aggregated_evaluators=aggregated_evaluators,
    )

    assert_evaluation_response(
        resp, 0, 1, n_aggregated_evaluators=len(aggregated_evaluators)
    )

    assert_evaluation_values(resp, aggregated_records=[("my_agg_v0", 0.0)])


def test_evaluate_with_basic_agg_eval():
    def my_agg_evaluator(df_example_level_metrics: pd.DataFrame) -> float:
        return 0.0

    aggregated_evaluators = dict(my_agg_v0=my_agg_evaluator)

    resp = e.evaluate(
        project_id=None,
        examples_dataframe=pd.DataFrame(
            {"query": ["x", "y"], "groundTruth": ["xgt", "ygt"]}
        ),
        aggregated_evaluators=dict(my_agg_v0=my_agg_evaluator),
    )

    assert_evaluation_response(
        resp, 0, 1, n_aggregated_evaluators=len(aggregated_evaluators)
    )

    assert_evaluation_values(
        resp,
        aggregated_records=[("my_agg_v0", 0.0)],
    )


def test_evaluate_with_df_and_ground_truth():
    queries = ["x", "y"]
    evaluators = {"exact_match"}
    resp = e.evaluate(
        project_id=None,
        examples_dataframe=pd.DataFrame(
            {"query": queries, "groundTruth": ["xgt", "ygt"]}
        ),
        evaluators=e.get_default_evaluators(evaluators),
    )

    assert_evaluation_response(resp, len(queries), len(evaluators))

    assert_evaluation_values(
        resp,
        [("exact_match", 0.0), ("exact_match", 0.0)],
        [
            ("exact_match_mean", 0.0),
            ("exact_match_std", 0.0),
            ("exact_match_count", 2.0),
        ],
    )


def test_evaluate_with_bad_df():
    try:
        resp = e.evaluate(
            project_id=None,
            examples_dataframe=pd.DataFrame({"some_col": ["x", "y"]}),
            evaluators=e.get_default_evaluators({"exact_match"}),
        )

        assert False, f"Expected ValueError, got {resp}"
    except ValueError as exn:
        assert "DataFrame must have a 'query' column" in str(exn)


def test_evaluate_with_df():
    queries = ["x", "y"]
    evaluators = {"exact_match"}
    resp = e.evaluate(
        project_id=None,
        examples_dataframe=pd.DataFrame({"query": queries}),
        evaluators=e.get_default_evaluators(evaluators),
    )

    assert_evaluation_response(resp, len(queries), len(evaluators))

    assert_evaluation_values(
        resp,
        [("exact_match", 1.0), ("exact_match", 1.0)],
        [
            ("exact_match_std", 0.0),
            ("exact_match_mean", 1.0),
            ("exact_match_count", 2.0),
        ],
    )


def test_evaluate_with_example_set_id():
    queries = ["x", "y"]
    evaluators = {"exact_match"}
    resp = e.evaluate(
        project_id=None,
        example_set_id="clwofniu5002uqprxtz5q4j6m",
        evaluators=e.get_default_evaluators(evaluators),
    )

    assert_evaluation_response(resp, len(queries), len(evaluators))

    assert_evaluation_values(
        resp,
        [("exact_match", 1.0), ("exact_match", 1.0)],
        [
            ("exact_match_std", 0.0),
            ("exact_match_count", 2.0),
            ("exact_match_mean", 1.0),
        ],
    )


def test_run_user_rag_query_function_with_bad_df():
    def rqfn(x: str) -> str:
        return f"This is the output. The query was: {x}"

    df_inputs = pd.DataFrame({"some_col": ["x", "y"]})

    try:
        out = e.run_query_function(
            rqfn,
            df_inputs,
        )

        assert False, f"Expected ValueError, got {out}"
    except ValueError as exn:
        expected = "Input set must have an 'input' or 'query' column"
        assert expected in str(exn), f"{str(exn)=}"


def test_run_user_rag_query_function_with_df():
    def rqfn(x: str) -> str:
        return f"This is the output. The query was: {x}"

    df_inputs = pd.DataFrame({"query": ["x", "y"]})

    out = e.run_query_function(
        rqfn,
        df_inputs,
    )

    assert out == [
        "This is the output. The query was: x",
        "This is the output. The query was: y",
    ], f"Got {out=}"


def test_run_user_rag_query_function():
    def rqfn(x: str) -> str:
        return f"This is the output. The query was: {x}"

    queries = ["x", "y"]

    out = e.run_query_function(
        rqfn,
        queries,
    )

    assert out == [
        "This is the output. The query was: x",
        "This is the output. The query was: y",
    ], f"Got {out=}"


def test_download_example_set():
    df = e.download_example_set(example_set_name="set4")
    # TODO: check stuff like name

    assert_df_conditions(
        df,
        rows=20,
        cols=17,
        cols_contain={
            "exampleId",
            "createdAt",
            "updatedAt",
            "query",
            "context",
            "fullyResolvedPrompt",
            "input",
            "output",
            "groundTruth",
            "metadata",
            "ragQueryTraceId",
            "ragEventId",
            "eventName",
            "exampleSetId",
            "ragQueryTrace",
            "exampleSetName",
        },
        # TODO: this seems flaky. Fix.
        # nulls_axis0=[0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 20, 0, 20, 20, 0, 0, 0],
        #     nulls_axis1=[
        #         4,
        #         4,
        #         4,
        #         4,
        #         4,
        #         4,
        #         4,
        #         4,
        #         4,
        #         4,
        #         4,
        #         4,
        #         4,
        #         3,
        #         4,
        #         3,
        #         4,
        #         3,
        #         3,
        #         3,
        #     ],
    )

    df = e.download_example_set(example_set_id="clwofniu5002uqprxtz5q4j6m")
    # TODO: check stuff like name
    assert_df_conditions(
        df,
        rows=2,
        cols=17,
        cols_contain={
            "exampleId",
            "createdAt",
            "updatedAt",
            "query",
            "context",
            "fullyResolvedPrompt",
            "input",
            "output",
            "groundTruth",
            "metadata",
            "ragQueryTraceId",
            "ragEventId",
            "eventName",
            "exampleSetId",
            "ragQueryTrace",
            "exampleSetName",
        },
        nulls_axis0=[
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            2,
            2,
            2,
            0,
            2,
            2,
            0,
            0,
            0,
        ],
        nulls_axis1=[5, 5],
    )


def test_create_example_set_no_ground_truth_from_rag_query_traces():
    def _download() -> pd.DataFrame:
        for df in e.download_query_traces(project_id=None, batch_limit=2):
            return df

        raise ValueError("No data found")

    df = _download()

    df["input"] = df["input"].fillna("input missing")  # type: ignore[pandas]

    resp = e.create_example_set(
        df=df,
        example_set_name="set5",
    )

    assert_example_set_create_response(
        resp,
        "set5",
        message_values_present={
            "id",
            "createdAt",
            "updatedAt",
            "name",
            "creatorId",
            "visibility",
            "active",
        },
    )


def test_craete_example_set_with_ground_truth_from_rag_query_traces():
    def _download() -> pd.DataFrame:
        for df in e.download_query_traces(project_id=None, batch_limit=2):
            return df

        raise ValueError("No data found")

    df = _download()

    df["input"] = df["input"].fillna("input missing")  # type: ignore[pandas]

    resp = e.create_example_set(
        df=df,
        example_set_name="set4",
        ground_truths=["xgt", "ygt"],
    )

    assert_example_set_create_response(
        resp,
        "set4",
        message_values_present={
            "id",
            "createdAt",
            "updatedAt",
            "name",
            "creatorId",
            "visibility",
            "active",
        },
    )


def test_download_query_set_by_name():
    # TODO: check stuff like name
    sets_with_gt = {"set1", "set3"}
    for setname in ["set1", "set2", "set3"]:
        logger.warning(f"Downloading setname={setname}")
        resp = e.download_query_set(query_set_name=setname)
        pdoptions(r=5, c=10, w=10, dw=None)

        n_cols_base = 8
        gt_cols: set[str] = (
            {"groundTruth"} if setname in sets_with_gt else set()
        )
        n_cols = n_cols_base + len(gt_cols)
        assert_df_conditions(
            resp,
            cols_contain={
                "queryId",
                "updatedAt",
                "input",
                "query",
                "querySetId",
                "createdAt",
                "querySetName",
            }
            | gt_cols,
            rows=20,
            cols=n_cols,
            nulls_axis0=[0] * n_cols,
            nulls_axis1=[
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
        )


def test_download_query_set_by_id():
    # TODO: check stuff like name
    sets_with_gt = {
        "clwoenwjo0039qymx70nk09k6",
        "clwoe4b4n003dpeijuzema4kb",
        "clwoegce1002qqymx26vndd0e",
    }
    for setid in [
        "clwoenwjo0039qymx70nk09k6",
        "clwoe4b4n003dpeijuzema4kb",
        "clwoe5rmf003apbpxyo3z2zss",
        "clwoegce1002qqymx26vndd0e",
    ]:
        logger.warning(f"Downloading setid={setid}")
        resp = e.download_query_set(query_set_id=setid)

        n_cols_base = 8
        gt_cols: set[str] = {"groundTruth"} if setid in sets_with_gt else set()
        n_cols = n_cols_base + len(gt_cols)
        assert_df_conditions(
            resp,
            cols_contain={
                "queryId",
                "updatedAt",
                "input",
                "query",
                "querySetId",
                "createdAt",
                "querySetName",
            },
            rows=2,
            cols=n_cols,
            nulls_axis0=[0] * n_cols,
        )


def test_create_query_set_with_name():
    resp = e.create_query_set(
        pd.DataFrame({"query": ["x", "y"]}),
        "set3",
        ["xgt", "ygt"],
    )

    assert_example_set_create_response(
        resp,
        "set3",
        message_values_present={
            "id",
            "createdAt",
            "updatedAt",
            "name",
            "creatorId",
            "visibility",
            "active",
        },
    )

    # Default name

    resp = e.create_query_set(
        pd.DataFrame({"query": ["x", "y"]}),
        ground_truths=["xgt", "ygt"],
    )

    assert_example_set_create_response(
        resp,
        "Query Set",
        message_values_present={
            "id",
            "createdAt",
            "updatedAt",
            "name",
            "creatorId",
            "visibility",
            "active",
        },
    )


def test_create_query_set_from_df_with_ground_truth():
    try:
        resp = e.create_query_set(
            pd.DataFrame({"some_col": ["x", "y"]}),
            "set3",
            ["xgt", "ygt"],
        )

        assert False, f"Expected ValueError, got {resp}"
    except ValueError as exn:
        expected = "The input set must contain a 'query' column."
        assert expected in str(exn), f"{str(exn)=}"


def test_create_query_set_no_ground_truth():
    resp = e.create_query_set(
        ["x", "y"],
        "set2",
    )

    assert_example_set_create_response(
        resp,
        "set2",
        message_values_present={
            "id",
            "createdAt",
            "updatedAt",
            "name",
            "creatorId",
            "visibility",
            "active",
        },
    )


def test_create_query_set_with_ground_truth():
    resp = e.create_query_set(
        ["x", "y"],
        "set1",
        ["xgt", "ygt"],
    )

    assert_example_set_create_response(
        resp,
        "set1",
        message_values_present={
            "id",
            "createdAt",
            "updatedAt",
            "name",
            "creatorId",
            "visibility",
            "active",
        },
    )
