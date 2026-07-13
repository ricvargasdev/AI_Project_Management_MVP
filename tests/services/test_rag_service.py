from app.services.rag_service import RAGService
from tests.fakes.fake_ai_client import FakeAIClient


def test_retrieve_projects_returns_results(db):

    #
    # Arrange
    #

    fake_ai = FakeAIClient()

    #
    # We'll create projects using the existing service
    #

    from app.services.project_service import ProjectService

    project_service = ProjectService(
        db=db,
        ai_client=fake_ai
    )

    project_service.create_project(
        customer_name="MHP",
        title="Users API",
        document="Customer requested three new fields."
    )

    project_service.create_project(
        customer_name="MHP",
        title="Users API",
        document="Customer requested API fields."
    )

    project_service.create_project(
        customer_name="MHP",
        title="Landing Page",
        document="Customer requested hero redesign."
    )

    project_service.create_project(
        customer_name="MHP",
        title="Checkout",
        document="Customer requested Stripe integration."
    )

    #
    # Act
    #

    rag = RAGService(
        db=db,
        ai_client=fake_ai
    )

    projects = rag.retrieve_projects(
        "MHP",
        "Users API"
    )

    #
    # Assert
    #

    assert len(projects) == 4

    assert projects[0].title == "Users API"