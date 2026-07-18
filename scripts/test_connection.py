from app.ai_client import AIClient

ai = AIClient()

answer = ai.chat(
    "In one sentence, what is PostgreSQL?"
)

print(answer)

embedding = ai.embed(
    "Customer MHP requested updates to the Users API."
)

print()
print(f"Embedding dimensions: {len(embedding)}")
print(f"First five values: {embedding[:5]}")