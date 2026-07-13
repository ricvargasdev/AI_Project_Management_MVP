from sqlalchemy.orm import Session

from app.ai_client import AIClient

from app.models.customer import Customer
from app.models.project import Project


class ProjectService:

    def __init__(
        self,
        db: Session,
        ai_client: AIClient
    ):
        self.db = db
        self.ai = ai_client

    def create_project(
        self,
        customer_name: str,
        title: str,
        document: str
    ):

        #
        # Find customer
        #

        customer = (
            self.db.query(Customer)
            .filter(Customer.name == customer_name)
            .first()
        )

        #
        # Create customer if necessary
        #

        if customer is None:

            customer = Customer(
                name=customer_name
            )

            self.db.add(customer)
            self.db.flush()

        #
        # Build project context
        #

        context = self.build_context(
            customer.name,
            title,
            document
        )

        #
        # Generate embedding
        #

        embedding = self.ai.embed(
            context
        )

        #
        # Create project
        #

        project = Project(
            customer_id=customer.id,
            title=title,
            document=document,
            embedding=embedding
        )

        self.db.add(project)

        self.db.commit()

        self.db.refresh(project)

        return project

    def build_context(
        self,
        customer,
        title,
        document
    ):

        return f"""
Customer:
{customer}

Project:
{title}

Description:
{document}
"""