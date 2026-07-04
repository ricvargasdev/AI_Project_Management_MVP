from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.project import CreateProjectRequest

from app.services.project_service import ProjectService

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.post("")
def create_project(
    request: CreateProjectRequest,
    db: Session = Depends(get_db)
):

    service = ProjectService(db)

    project = service.create_project(
        customer_name=request.customer,
        title=request.title,
        document=request.document
    )

    return {
        "id": project.id,
        "title": project.title
    }