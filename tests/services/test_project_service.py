from app.models.customer import Customer
from app.services.project_service import ProjectService
from tests.fakes.fake_ai_client import FakeAIClient


def test_create_project_creates_new_customer(db):

    fake_ai = FakeAIClient()

    service = ProjectService(
        db=db,
        ai_client=fake_ai
    )

    project = service.create_project(
        customer_name="MHP",
        title="Users API",
        document="Customer requested new API fields."
    )

    customer = (
        db.query(Customer)
        .filter(Customer.name == "MHP")
        .first()
    )

    assert customer is not None
    assert project.customer_id == customer.id
    assert project.title == "Users API"
    assert project.document == "Customer requested new API fields."


def test_create_project_reuses_existing_customer(db):

    customer = Customer(
        name="MHP"
    )

    db.add(customer)
    db.commit()

    fake_ai = FakeAIClient()

    service = ProjectService(
        db=db,
        ai_client=fake_ai
    )

    service.create_project(
        customer_name="MHP",
        title="Another Project",
        document="Another document"
    )

    customers = (
        db.query(Customer)
        .filter(Customer.name == "MHP")
        .all()
    )

    assert len(customers) == 1


def test_create_project_generates_embedding(db):

    fake_ai = FakeAIClient()

    service = ProjectService(
        db=db,
        ai_client=fake_ai
    )

    project = service.create_project(
        customer_name="MHP",
        title="Users API",
        document="Customer requested new API fields."
    )

    assert fake_ai.called is True
    assert project.embedding is not None
    assert len(project.embedding) == 768


def test_create_project_builds_correct_context(db):

    fake_ai = FakeAIClient()

    service = ProjectService(
        db=db,
        ai_client=fake_ai
    )

    service.create_project(
        customer_name="MHP",
        title="Users API",
        document="Customer requested new API fields."
    )

    assert fake_ai.called is True

    assert "MHP" in fake_ai.last_text
    assert "Users API" in fake_ai.last_text
    assert "Customer requested new API fields." in fake_ai.last_text


def test_build_context():

    service = ProjectService(
        db=None,
        ai_client=None
    )

    context = service.build_context(
        customer="MHP",
        title="Users API",
        document="Added three fields"
    )

    assert "MHP" in context
    assert "Users API" in context
    assert "Added three fields" in context