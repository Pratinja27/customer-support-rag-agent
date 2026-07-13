from langgraph.graph import StateGraph, START, END

from src.state import GraphState
from src.rag import retrieve_documents, generate_answer


def retrieve_node(state: GraphState):
    """
    Retrieve relevant documents from ChromaDB.
    """

    question = state["question"]

    docs = retrieve_documents(question)

    return {
        "question": question,
        "retrieved_docs": docs,
    }


def generate_node(state: GraphState):
    """
    Generate an answer using Gemini.
    """

    answer = generate_answer(
        state["question"],
        state["retrieved_docs"],
    )

    return {
        "answer": answer,
    }


builder = StateGraph(GraphState)

builder.add_node("retrieve", retrieve_node)
builder.add_node("generate", generate_node)

builder.add_edge(START, "retrieve")
builder.add_edge("retrieve", "generate")
builder.add_edge("generate", END)

graph = builder.compile()