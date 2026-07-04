from sqlalchemy.orm import Session

from app.models.customer import Customer
from app.models.project import Project

from app.repositories.customer_repository import CustomerRepository
from app.repositories.project_repository import ProjectRepository

from app.services.embedding_service import EmbeddingService


class ProjectService:

    def __init__(self, db: Session):

        self.db = db

        self.customer_repository = CustomerRepository(db)
        self.project_repository = ProjectRepository(db)

        self.embedding_service = EmbeddingService()

    def create_project(
        self,
        customer_name: str,
        title: str,
        document: str
    ):

        customer = self.customer_repository.find_by_name(customer_name)

        if customer is None:

            customer = Customer(
                name=customer_name
            )

            self.db.add(customer)
            self.db.commit()
            self.db.refresh(customer)

        embedding = self.embedding_service.generate(document)

        project = Project(
            customer_id=customer.id,
            title=title,
            document=document,
            embedding=embedding
        )

        return self.project_repository.save(project)