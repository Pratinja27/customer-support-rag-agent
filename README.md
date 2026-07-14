# customer-support-rag-agent
Customer Support RAG Agent built with LangGraph, Gemini, ChromaDB, and Streamlit featuring conversational memory, source citations, and retrieval-augmented generation (RAG).


# GigaCorp Customer Support Assistant

## Overview

GigaCorp Customer Support Assistant is an AI-powered customer support chatbot that answers user queries using Retrieval-Augmented Generation (RAG). The application retrieves relevant information from a company knowledge base stored in ChromaDB and generates context-aware responses using Google Gemini. It also maintains conversation history to support follow-up questions.

---

## Features

* Retrieval-Augmented Generation (RAG)
* Semantic document search using ChromaDB
* Context-aware conversations with chat history
* Google Gemini-powered response generation
* Source document references for transparency
* Support for PDF and text-based knowledge bases
* Interactive Streamlit web interface

---

## Technology Stack

* Python
* Streamlit
* LangChain
* LangGraph
* Google Gemini
* ChromaDB
* HuggingFace Embeddings
* Sentence Transformers
* PyPDF
* Python Dotenv

---

## Project Structure

```text
.
├── app.py
├── requirements.txt
├── data/
├── chroma_db/
├── src/
│   ├── graph.py
│   ├── llm.py
│   ├── rag.py
│   ├── state.py
│   └── vector_store.py
└── README.md
```

---

## Prerequisites

* Python 3.11 or 3.12
* Google Gemini API Key

---

## Installation

### Clone the repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_google_gemini_api_key
```

---

## Building the Vector Database

Whenever documents in the `data` folder are added or updated, regenerate the vector database by running:

```bash
python src/vector_store.py
```

This creates the `chroma_db` directory containing the document embeddings used during retrieval.

---

## Running the Application

```bash
streamlit run app.py
```

---

## Example Queries

* Do you ship to India?
* What are your business hours?
* What is your return policy?
* Which subscription plans are available?
* How long does shipping take?

---

## How the System Works

1. Documents are loaded from the `data` folder.
2. Documents are split into smaller chunks.
3. HuggingFace embeddings are generated for each chunk.
4. Embeddings are stored in ChromaDB.
5. User questions are converted into embeddings.
6. The retriever searches ChromaDB for relevant document chunks.
7. Retrieved context and conversation history are passed to Google Gemini.
8. The assistant generates an answer using only the retrieved company knowledge.

---

## Deployment

The application can be deployed on platforms such as:

* Streamlit Community Cloud
* Render
* Railway

---

## License

This project was developed for educational purposes as part of an AI Customer Support Assistant assignment.
