from sqlalchemy import text

from app.ai_client import AIClient
from app.database import engine

ai = AIClient()

document = """
Customer: MHP

Project: API Improvements

Summary:
Customer requested additional fields for the Users API endpoint.

Tasks:
- Add customerType
- Add startDate
- Update endpoint documentation

Notes:
Maintain backwards compatibility.
"""

embedding = ai.embed(document)

print(f"Embedding dimensions: {len(embedding)}")

with engine.begin() as conn:

    conn.execute(
        text("""
            INSERT INTO customers(name)
            VALUES (:name)
            ON CONFLICT (name)
            DO NOTHING
        """),
        {
            "name": "MHP"
        }
    )

    customer_id = conn.execute(
        text("""
            SELECT id
            FROM customers
            WHERE name = :name
        """),
        {
            "name": "MHP"
        }
    ).scalar_one()

    conn.execute(
        text("""
            INSERT INTO projects
            (
                customer_id,
                title,
                document,
                embedding
            )
            VALUES
            (
                :customer_id,
                :title,
                :document,
                :embedding
            )
        """),
        {
            "customer_id": customer_id,
            "title": "API Improvements",
            "document": document,
            "embedding": embedding
        }
    )

print("Project stored successfully!")