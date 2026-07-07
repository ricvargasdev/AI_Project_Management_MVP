from sqlalchemy.orm import Session

from app.models.customer import Customer
from app.models.project import Project

class ProjectService:

    def __init__(self, db: Session):

        self.db = db
