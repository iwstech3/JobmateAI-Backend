from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from typing import Generator
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Render specific optimizations
connect_args = {}
if "render.com" in DATABASE_URL or "internal" in DATABASE_URL:
    # Internal Render connections often prefer or require specific SSL handling
    # If the decryption error persists, we might need sslmode=disable here for internal
    connect_args["sslmode"] = "prefer"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=300,  # More aggressive recycle for cloud databases
    pool_size=5,       # Lower pool size to stay within free tier limits
    max_overflow=10,
    connect_args=connect_args
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Add this function - it was missing!
def get_db() -> Generator[Session, None, None]:
    """
    Dependency that provides a database session to route handlers.
    Automatically closes the session after the request completes.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()