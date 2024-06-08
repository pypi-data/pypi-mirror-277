from __future__ import annotations

import operator
from enum import Enum
from typing import Annotated, Sequence, TypedDict, Union

from langchain_core.pydantic_v1 import BaseModel


class CitationType(Enum):
    DOCUMENT = "Document"
    REPORT = "Report"


class Citation(BaseModel):
    label: str
    """The citation label to show the user."""

    citation_type: CitationType = CitationType.DOCUMENT
    """The type of this citation."""

    report_query: str = ""
    """The associated query (if any), in case of a report type citation."""

    document_id: str = ""
    """The associated document ID (if known), in case of a document type citation."""


class CitedAnswer(BaseModel):
    source: str
    answer: str
    citations: list[Citation] = []
    is_final: bool = False
    metadata: dict = {}


class Invocation(BaseModel):
    tool_name: str
    tool_input: str
    log: str = ""

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Invocation):
            return NotImplemented

        # Compare tool_name and tool_input for equality
        return (self.tool_name, self.tool_input) == (other.tool_name, other.tool_input)


class StepState(BaseModel):
    output: str
    invocation: Invocation
    citations: list[Citation] = []

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, StepState):
            return NotImplemented

        # Compare invocation and output for equality
        return (self.invocation, self.output) == (other.invocation, other.output)


class AgentState(TypedDict):
    # **** Inputs
    # The list of previous messages in the conversation
    chat_history: list[tuple[str, str]]

    # The input question
    question: str

    # **** Internal State

    # Names of all tools available to the agent
    tool_names: Union[str, None]

    # Descriptions of all tools available to the agent
    tool_descriptions: Union[str, None]

    # The next tool invocation that must be made
    tool_invocation: Union[Invocation, None]

    # List of steps taken so far (this state is added to, not overwritten)
    intermediate_steps: Annotated[Sequence[StepState], operator.add]

    # **** Output
    cited_answer: CitedAnswer
