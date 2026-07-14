from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage, AIMessage

from src.state import GraphState
from src.rag import retrieve_documents, generate_answer


def retrieve_node(state: GraphState):
    question = state["question"]

    docs = retrieve_documents(question)

    return {
        "question": question,
        "retrieved_docs": docs,
        "messages": state.get("messages", []),
    }


def generate_node(state: GraphState):

    history = state.get("messages", [])

    answer = generate_answer(
        question=state["question"],
        docs=state["retrieved_docs"],
        history=history,
    )

    updated_messages = history + [
        HumanMessage(content=state["question"]),
        AIMessage(content=answer),
    ]

    return {
        "question": state["question"],
        "retrieved_docs": state["retrieved_docs"],
        "answer": answer,
        "messages": updated_messages,
    }


builder = StateGraph(GraphState)

builder.add_node("retrieve", retrieve_node)
builder.add_node("generate", generate_node)

builder.add_edge(START, "retrieve")
builder.add_edge("retrieve", "generate")
builder.add_edge("generate", END)

memory = MemorySaver()

graph = builder.compile(
    checkpointer=memory
)