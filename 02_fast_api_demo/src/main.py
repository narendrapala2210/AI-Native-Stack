from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.config.settings import get_settings
from src.controllers.book_controller import router as book_router
from src.database.base import Base
from src.database.session import engine
from src.models import Book  # noqa: F401 - registers the model with SQLAlchemy


@asynccontextmanager
async def lifespan(_: FastAPI):
	Base.metadata.create_all(bind=engine)
	yield


settings = get_settings()
app = FastAPI(title=settings.app_name, version="1.0.0", lifespan=lifespan)
app.include_router(book_router, prefix="/api/v1")


@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
	return {"status": "ok", "environment": settings.app_env}
