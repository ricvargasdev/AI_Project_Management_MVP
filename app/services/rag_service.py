from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.project import Project


class RAGService:

    def __init__(self, db: Session):

        self.db = db

    def ask(self, customer: str, question: str):

        question_embedding = self.ai.embed(question)

        projects = (
            self.db.query(Project)
            .join(Project.customer)
            .filter_by(name=customer)
            .order_by(
                Project.embedding.cosine_distance(question_embedding)
            )
            .limit(3)
            .all()
        )

        context = ""

        for project in projects:

            context += f"""

                Project:
                {project.title}

                {project.document}

                ------------------------

                """

            prompt = f"""
                You are an AI assistant for a software development agency.

                Answer ONLY using the supplied context.

                If you don't know, say so.

                Context:

                {context}

                Question:

                {question}
                """

        return self.ai.chat(prompt)