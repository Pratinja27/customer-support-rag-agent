# Customer Support RAG Agent

An AI-powered customer support assistant built with **LangGraph**, **Google Gemini**, **ChromaDB**, and **Streamlit**. The application uses Retrieval-Augmented Generation (RAG) to answer customer queries based on a custom knowledge base while maintaining conversational context across interactions.

---

## Overview

The Customer Support RAG Agent retrieves relevant information from a company knowledge base and uses Google Gemini to generate accurate, context-aware responses. By combining semantic search with a large language model, the assistant minimizes hallucinations and answers questions using only the available documentation.

---

## Features

* Retrieval-Augmented Generation (RAG)
* Conversational memory for follow-up questions
* Semantic document retrieval using ChromaDB
* Google Gemini-powered response generation
* Source citations for retrieved information
* Support for PDF and text documents
* Interactive Streamlit user interface
* Modular LangGraph workflow

---

## Technology Stack

* Python
* Streamlit
* LangGraph
* LangChain
* LangChain Chroma
* LangChain Google Generative AI
* ChromaDB
* Hugging Face Embeddings
* Sentence Transformers
* PyPDF
* python-dotenv

---

## Project Structure

```text
customer-support-rag-agent/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
│
├── data/
│
├── chroma_db/
│
└── src/
    ├── graph.py
    ├── llm.py
    ├── rag.py
    ├── state.py
    └── vector_store.py
```

---

## Prerequisites

* Python 3.11 or later
* Google Gemini API Key

---

## Installation

### Clone the repository

```bash
git clone https://github.com/<your-username>/customer-support-rag-agent.git
cd customer-support-rag-agent
```

### Create and activate a virtual environment

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
GOOGLE_API_KEY=your_google_api_key
```

---

## Creating the Vector Database

Whenever documents are added to or updated in the `data` directory, regenerate the vector database:

```bash
python src/vector_store.py
```

This creates or updates the `chroma_db` directory, which stores the document embeddings used during retrieval.

---

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

---

## Example Queries

* What is your return policy?
* How long does shipping take?
* Do you offer international shipping?
* What subscription plans are available?
* What are your customer support hours?

---

## How It Works

1. Documents are loaded from the `data` directory.
2. Documents are split into smaller chunks.
3. Hugging Face embeddings are generated for each chunk.
4. Embeddings are stored in ChromaDB.
5. The user's question is converted into an embedding.
6. The retriever finds the most relevant document chunks.
7. Retrieved context and conversation history are passed to Google Gemini.
8. Gemini generates an answer grounded in the retrieved knowledge.
9. The assistant returns the response along with the relevant source references.

---

## Deployment

The application can be deployed on platforms such as:

* Render
* Streamlit Community Cloud
* Railway

---

## Future Improvements

* Multi-document support
* Conversation history persistence
* User authentication
* Admin dashboard for document management
* Support for additional LLM providers
* Streaming responses

---

## License

This project was developed for educational purposes as part of an AI Customer Support Assistant assignment.
