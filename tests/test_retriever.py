from src.rag import get_retriever

retriever = get_retriever()

docs = retriever.invoke("Do you ship to India?")

for i, doc in enumerate(docs, start=1):
    print(f"\n----- Result {i} -----")
    print(doc.page_content)
    print("\nSource:", doc.metadata)
    