from src.rag import answer_question

question = "Do you ship to India?"

result = answer_question(question)

print("\nQUESTION")
print(question)

print("\nANSWER")
print(result["answer"])

print("\nSOURCES")

for i, doc in enumerate(result["documents"], start=1):
    print(f"\nSource {i}")
    print(doc.metadata)