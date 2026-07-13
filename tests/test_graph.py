from src.graph import graph

response = graph.invoke(
    {
        "question": "Do you ship to India?"
    }
)

print("\nAnswer:\n")
print(response["answer"])