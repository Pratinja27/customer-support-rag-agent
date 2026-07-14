from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

DATA_FOLDER = "data"
CHROMA_PATH = "chroma_db"

def load_documents():
    documents = []

    for file in DATA_FOLDER.iterdir():

        if file.suffix == ".pdf":
            loader = PyPDFLoader(str(file))
            documents.extend(loader.load())

        elif file.suffix in [".md", ".txt"]:
            loader = TextLoader(str(file), encoding="utf-8")
            documents.extend(loader.load())

    return documents


def create_vector_store():

    print("Loading documents...")

    docs = load_documents()

    print(f"Loaded {len(docs)} documents.")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
    )

    chunks = splitter.split_documents(docs)

    print(f"Created {len(chunks)} chunks.")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(CHROMA_PATH),    )
    print("Vector Store Count:", db._collection.count())    
    print("Vector database created successfully!")
    
    return db


if __name__ == "__main__":
    create_vector_store()

