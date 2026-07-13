import pytest

from app.database import SessionLocal
from app.models.customer import Customer
from app.models.project import Project


@pytest.fixture
def db():

    session = SessionLocal()

    #
    # Start every test with an empty database
    #

    session.query(Project).delete()
    session.query(Customer).delete()

    session.commit()

    yield session

    session.close()