from fastapi import FastAPI

from .db import Base, engine

# Import models to ensure they are registered with SQLAlchemy
from . import models  # noqa: F401

# Create all tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="MetaOps", version="0.1.0")


@app.get("/health")
def health():
    """Health check endpoint."""
    return {"status": "ok"}
