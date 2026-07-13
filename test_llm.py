from src.llm import get_llm

llm = get_llm()

response = llm.invoke("Reply with exactly: Gemini Connected!")

print(response.content)