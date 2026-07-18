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
        customer_name: str,
        projects,
        question: str
    ):

        project_history = ""

        for project in projects:

            project_history += f"""
        Project Title:
        {project.title}

        Project Details:
        {project.document}

        ----------------------------------------
        """

            prompt = f"""
        You are an experienced Technical Project Manager.

        You answer questions ONLY using the project history below.

        Rules:

        1. Never invent information.
        2. Never use external knowledge.
        3. If the answer cannot be found, reply exactly:
        "I couldn't find that information in the customer's project history."
        4. Mention the project title whenever possible.
        5. Keep your answer concise.

        Customer:
        {customer_name}

        ========================================

        PROJECT HISTORY

        {project_history}

        ========================================

        QUESTION

        {question}
        """

        return prompt

    def answer_question(
        self,
        customer_name: str,
        question: str
    ):
        projects = self.retrieve_projects(
            customer_name=customer_name,
            question=question
        )

        if not projects:
            return "I couldn't find any projects for that customer."

        prompt = self.build_prompt(
            customer_name=customer_name,
            projects=projects,
            question=question
        )

        return self.ai.chat(prompt)