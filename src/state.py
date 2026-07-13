from typing import TypedDict

from langchain_core.documents import Document


class GraphState(TypedDict):
    """
    Shared state across all LangGraph nodes.
    """

    question: str
    retrieved_docs: list[Document]
    answer: str