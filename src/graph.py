from langgraph.graph import StateGraph, START, END

from src.state import GraphState
from src.rag import answer_question


def rag_node(state: GraphState):
    """
    Execute the RAG pipeline.
    """

    result = answer_question(state["question"])

    return {
        "question": state["question"],
        "retrieved_docs": result["documents"],
        "answer": result["answer"],
    }


builder = StateGraph(GraphState)

builder.add_node("rag", rag_node)

builder.add_edge(START, "rag")

builder.add_edge("rag", END)

graph = builder.compile()