from app.ai_client import AIClient
from app.vector_store import VectorStore

ai = AIClient()

customer_name = "MHP"

question = "When did MHP request updates to the Users API?"

embedding = ai.embed(question)

rows = VectorStore.search(
    customer_name=customer_name,
    embedding=embedding
)

for row in rows:

    print("----------------------------------")
    print(f"Project : {row.title}")
    print(f"Distance: {row.distance:.4f}")
    print()
    print(row.document)