from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud
from app.api import schemes
from app.core.database import database

router: APIRouter = APIRouter(
    prefix="/users",
)


@router.get(
    "",
    summary="Получить информацию o всех пользователях",
    description="Boзвpaщaeт информацию o всех пользователях.",
    responses={
        status.HTTP_200_OK: {},
    },
)
async def get_users(
    session: Annotated[
        AsyncSession,
        Depends(database.get_scoped_session),
    ],
) -> JSONResponse:
    return JSONResponse(
        content=schemes.UserList.from_models(
            await crud.get_users_all(session=session),
        ).model_dump(mode="json"),
        status_code=status.HTTP_200_OK,
    )
