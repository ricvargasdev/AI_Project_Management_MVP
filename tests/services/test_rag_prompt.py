from app.services.rag_service import RAGService


class Project:

    def __init__(self, title, document):
        self.title = title
        self.document = document


def test_build_prompt_contains_projects_and_question():

    rag = RAGService(
        db=None,
        ai_client=None
    )

    projects = [

        Project(
            "Users API",
            "Customer requested three new API fields."
        ),

        Project(
            "Landing Page",
            "Customer requested a new hero section."
        )

    ]

    prompt = rag.build_prompt(

        projects=projects,

        question="When did MHP request API changes?"

    )

    assert "Never invent or make up information" in prompt

    assert "ONLY" in prompt

    assert "PROJECT HISTORY" in prompt