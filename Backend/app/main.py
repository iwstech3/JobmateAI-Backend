from fastapi import FastAPI
from app.core.config import settings
from app.api import auth
from app.database.base import Base
from app.database.session import engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])

@app.get("/")
def read_root():
    return {"message": "Welcome to JobmateAI Backend"}
