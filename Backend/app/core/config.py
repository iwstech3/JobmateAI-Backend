from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "JobmateAI Backend"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "YOUR_SECRET_KEY_HERE_PLEASE_CHANGE_IT" # TODO: Change this in production
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8 # 8 days
    ALGORITHM: str = "HS256"
    
    SQLALCHEMY_DATABASE_URI: Optional[str] = "sqlite:///./sql_app.db"

    class Config:
        case_sensitive = True

settings = Settings()
