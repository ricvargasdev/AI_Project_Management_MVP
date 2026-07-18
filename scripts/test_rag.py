from app.ai_client import AIClient
from app.database import SessionLocal
from app.services.rag_service import RAGService


db = SessionLocal()

rag = RAGService(
    db=db,
    ai_client=AIClient()
)

answer = rag.answer_question(
    # customer_name="MHP",
    # question="When did MHP request updates to the Users API?"
    customer_name="Acme Ltd",
    question="Has Acme Ltd ever requested Stripe integration?"
)

print()
print("--------------------------------")
print(answer)
print("--------------------------------")