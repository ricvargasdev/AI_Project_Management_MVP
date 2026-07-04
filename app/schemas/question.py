from pydantic import BaseModel


class AskQuestionRequest(BaseModel):

    customer: str

    question: str


class AskQuestionResponse(BaseModel):

    answer: str