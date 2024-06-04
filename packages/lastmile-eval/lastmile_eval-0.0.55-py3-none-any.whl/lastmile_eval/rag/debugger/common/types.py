"""
Utils file for defining types used in the tracing SDK
"""

from dataclasses import dataclass
from typing import ParamSpec, Optional

T_ParamSpec = ParamSpec("T_ParamSpec")


# FYI: kw_only is needed due to position args with default values
# being delcared before non-default args. This is only supported on
# python 3.10 and above
@dataclass(kw_only=True)
class Node:
    """Node used during ingestion"""

    id: str
    title: Optional[str] = None
    text: str


@dataclass(kw_only=True)
class RetrievedNode(Node):
    """Node used during retrieval that also adds a retrieval score"""

    score: float
