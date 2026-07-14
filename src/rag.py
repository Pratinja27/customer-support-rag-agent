from pathlib import Path

from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate

from src.llm import get_llm
CHROMA_PATH = "chroma_db"
PROMPT = ChatPromptTemplate.from_template("""
You are GigaCorp's Customer Support Assistant.

Use BOTH:
1. Conversation History
2. Company Context

Rules:
- Use conversation history to understand follow-up questions such as "there", "that", "it", "those", etc.
- Answer ONLY using the company context.
- Do not invent information.
- If the answer is not present in the context, reply exactly:

"I couldn't find that information in the company's knowledge base."

Conversation History:
{history}

Company Context:
{context}

Question:
{question}

Answer:
""")


def get_vector_store():

    import os

    print("CURRENT DIRECTORY:")
    print(os.getcwd())

    print("FILES:")
    print(os.listdir())

    print("CHROMA FILES:")
    print(os.listdir("chroma_db"))

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings,
    )

    print("TOTAL CHUNKS:", db._collection.count())

    return db


def get_retriever():
    return get_vector_store().as_retriever(
        search_kwargs={"k": 4}
    )


def retrieve_documents(question):
    print("STEP 1: Starting retrieval")

    retriever = get_retriever()

    print("STEP 2: Retriever created")

    docs = retriever.invoke(question)

    print("STEP 3: Retrieved", len(docs), "documents")

    return docs


def format_history(history):

    if not history:
        return "No previous conversation."

    text = []

    for msg in history:

        if isinstance(msg, HumanMessage):
            text.append(f"User: {msg.content}")

        elif isinstance(msg, AIMessage):
            text.append(f"Assistant: {msg.content}")

    return "\n".join(text)


def generate_answer(question, docs, history):

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    history_text = format_history(history)

    llm = get_llm()

    chain = PROMPT | llm

    print("STEP 4: Calling Gemini")

    response = chain.invoke(
        {
            "history": history_text,
            "context": context,
            "question": question,
        }
    )

    print("STEP 5: Gemini responded")

    return response.content

def answer_question(question):

    docs = retrieve_documents(question)

    answer = generate_answer(
        question,
        docs,
        [],
    )

    return {
        "answer": answer,
        "documents": docs,
    }