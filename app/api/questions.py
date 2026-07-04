from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.question import AskQuestionRequest

from app.services.rag_service import RAGService

router = APIRouter(
    prefix="/questions",
    tags=["Questions"]
)


@router.post("")
def ask_question(
    request: AskQuestionRequest,
    db: Session = Depends(get_db)
):

    service = RAGService(db)

    answer = service.ask(
        customer=request.customer,
        question=request.question
    )

    return {
        "answer": answer
    }