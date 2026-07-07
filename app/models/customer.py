from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database import Base
from typing import TYPE_CHECKING, List
if TYPE_CHECKING:
    from app.models.project import Project


class Customer(Base):

    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(255),
        unique=True
    )

    projects: Mapped[List["Project"]] = relationship(
        "Project",
        back_populates="customer"
    )