from pydantic import BaseModel


class QuestionRequest(BaseModel):

    customer: str
    question: str


class QuestionResponse(BaseModel):

    answer: str