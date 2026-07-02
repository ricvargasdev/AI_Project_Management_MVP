from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from pgvector.sqlalchemy import Vector

from app.database import Base


class Customer(Base):

    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True
    )

    projects = relationship("Project")


class Project(Base):

    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customers.id")
    )

    title: Mapped[str] = mapped_column(
        String(255)
    )

    document: Mapped[str] = mapped_column(Text)

    embedding = mapped_column(Vector(768))

    customer = relationship("Customer")