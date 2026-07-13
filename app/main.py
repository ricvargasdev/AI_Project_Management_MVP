from fastapi import FastAPI

from app.api.customers import router as customer_router
from app.api.projects import router as project_router

app = FastAPI(
    title="AI Project Management MVP",
    version="0.1"
)

app.include_router(customer_router)
app.include_router(project_router)

@app.get("/")
def root():
    return {
        "application": "AI Project Management MVP",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "UP"
    }