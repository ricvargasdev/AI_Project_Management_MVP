from sqlalchemy import text

from app.database import engine


class VectorStore:

    @staticmethod
    def to_pgvector(vector: list[float]) -> str:
        return "[" + ",".join(map(str, vector)) + "]"

    @staticmethod
    def search(customer_name: str, embedding: list[float], limit: int = 3):

        vector = VectorStore.to_pgvector(embedding)

        with engine.connect() as conn:

            rows = conn.execute(
                text("""
                    SELECT
                        p.id,
                        p.title,
                        p.document,
                        p.embedding <=> CAST(:embedding AS vector) AS distance
                    FROM projects p
                    JOIN customers c
                        ON c.id = p.customer_id
                    WHERE c.name = :customer_name
                    ORDER BY p.embedding <=> CAST(:embedding AS vector)
                    LIMIT :limit
                """),
                {
                    "embedding": vector,
                    "customer_name": customer_name,
                    "limit": limit
                }
            )

            return rows.fetchall()