from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import jobs, documents, applications, saved_jobs, analytics, compatibility, generation
from app.database.db import Base, engine
from app.models import job_post, document  # ← Add document

import logging
import os

from contextlib import asynccontextmanager

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    try:
        logger.info("Verifying database connection and creating tables...")
        # Dispose of any engine connection created during import/fork phase
        engine.dispose()
        Base.metadata.create_all(bind=engine)
        logger.info("Database initialized successfully.")
    except Exception as e:
        logger.error(f"Error during database initialization: {e}")
    
    yield
    # Shutdown logic (if any)

app = FastAPI(
    title="JobMate AI API",
    description="AI-driven recruitment assistant platform",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(jobs.router, prefix="/api/v1")
app.include_router(documents.router, prefix="/api/v1")
app.include_router(applications.router, prefix="/api/v1")
app.include_router(saved_jobs.router, prefix="/api/v1")
app.include_router(analytics.router, prefix="/api/v1")
app.include_router(compatibility.router, prefix="/api/v1")
app.include_router(generation.router, prefix="/api/v1")


@app.get("/")
def root():
    """Health check endpoint"""
    return {
        "message": "JobMate AI API is running",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "database": "connected"
    }