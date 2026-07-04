from fastapi import FastAPI

from app.api.projects import router as project_router
from app.api.questions import router as question_router

app = FastAPI(
    title="AI Project Management MVP"
)

app.include_router(project_router)

app.include_router(question_router)