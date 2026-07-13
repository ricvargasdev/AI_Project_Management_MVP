from sqlalchemy import select, text
from sqlalchemy.orm import Session

from app.ai_client import AIClient
from app.models.customer import Customer
from app.models.project import Project


class RAGService:

    def __init__(
        self,
        db: Session,
        ai_client: AIClient
    ):
        self.db = db
        self.ai = ai_client

    def retrieve_projects(
        self,
        customer_name: str,
        question: str,
        limit: int = 10
    ):
        embedding = self.ai.embed(question)
        customer = (
            self.db.query(Customer)
            .filter(
                Customer.name == customer_name
            )
            .first()
        )

        if customer is None:
            return []

        projects = (
            self.db.query(Project)
            .filter(
                Project.customer_id == customer.id
            )
            .order_by(
                Project.embedding.cosine_distance(
                    embedding
                )
            )
            .limit(limit)
            .all()
        )
        return projects

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
    
    def build_prompt(
        self,
        projects,
        question
    ):
        context = ""
        for project in projects:

            context += f"""
    Project
    -------

    Title:
    {project.title}

    Description:
    {project.document}

    """

        return f"""
    You are a Senior Project Manager.

    You answer questions using ONLY the supplied project history.

    Rules

    1. Never invent or make up information.

    2. Never mention projects that are not in the context.

    3. If you don't know the answer, say:

    "I couldn't find that information."

    4. Mention the project title whenever possible.

    5. Be concise.

    ----------------------------

    PROJECT HISTORY

    {context}

    ----------------------------

    QUESTION

    {question}
    """

    def answer_question(
        customer_name,
        question
    ):

        projects = self.retrieve_projects(...)

        prompt = self.build_prompt(...)

        answer = self.ai.chat(prompt)

        return answer