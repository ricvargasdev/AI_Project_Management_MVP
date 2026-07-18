from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.ai_client import AIClient
from app.database import get_db
from app.schemas.question import QuestionRequest, QuestionResponse
from app.services.rag_service import RAGService

router = APIRouter(
    prefix="/questions",
    tags=["Questions"]
)

@router.post("")
def ask_question(
    request: QuestionRequest,
    db: Session = Depends(get_db)
):

    service = RAGService(
        db=db,
        ai_client=AIClient()
    )

    answer = service.answer_question(
        customer_name=request.customer,
        question=request.question
    )

    return QuestionResponse(
        answer=answer
    )