from pydantic import BaseModel


class CreateProjectRequest(BaseModel):

    customer: str

    title: str

    document: str


class ProjectResponse(BaseModel):

    id: int

    title: str

    customer: str

    class Config:
        from_attributes = True