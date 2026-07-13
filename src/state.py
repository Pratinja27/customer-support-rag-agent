from typing import Annotated

from langchain_core.documents import Document
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict


class GraphState(TypedDict):
    messages: Annotated[list, add_messages]
    question: str
    retrieved_docs: list[Document]
    answer: str