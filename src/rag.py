from pathlib import Path

from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate

from src.llm import get_llm

BASE_DIR = Path(__file__).resolve().parent.parent
CHROMA_PATH = BASE_DIR / "chroma_db"


def get_retriever():
    """
    Load the existing ChromaDB and return a retriever.
    """

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = Chroma(
        persist_directory=str(CHROMA_PATH),
        embedding_function=embeddings,
    )

    return vector_store.as_retriever(search_kwargs={"k": 3})


PROMPT = ChatPromptTemplate.from_template(
    """
You are a customer support assistant for GigaCorp.

Answer ONLY using the information provided in the context.

If the answer is not present in the context, say:

"I couldn't find that information in the company's knowledge base."

Context:
{context}

Question:
{question}
"""
)


def answer_question(question: str):
    """
    Retrieve relevant documents and generate an answer using Gemini.
    """

    retriever = get_retriever()

    docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in docs)

    llm = get_llm()

    chain = PROMPT | llm

    response = chain.invoke(
        {
            "context": context,
            "question": question,
        }
    )

    return {
        "answer": response.content,
        "documents": docs,
    }