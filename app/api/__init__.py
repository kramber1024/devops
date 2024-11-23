from fastapi import APIRouter

from .routes import users

api: APIRouter = APIRouter(
    prefix="/api",
)
api.include_router(users.router, tags=["Users"])

__all__ = ["api"]
