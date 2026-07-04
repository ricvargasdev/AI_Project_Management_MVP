from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from pgvector.sqlalchemy import Vector

from app.database import Base


class Project(Base):

    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customers.id")
    )

    title: Mapped[str] = mapped_column(
        String(255)
    )

    document: Mapped[str]

    embedding: Mapped[list[float]] = mapped_column(
        Vector(768)
    )

    customer = relationship(
        "Customer",
        back_populates="projects"
    )