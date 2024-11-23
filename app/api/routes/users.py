from typing import TYPE_CHECKING, Annotated

from fastapi import APIRouter, Body, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud
from app.api import schemes
from app.core.database import database

if TYPE_CHECKING:
    from app.core.database.models import User

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


@router.post(
    "",
    summary="Создать нового пользователя",
    description=(
        "Создает нового пользователя и возвращает его идентификатор."  # noqa: RUF001
    ),
    responses={
        status.HTTP_201_CREATED: {},
    },
)
async def create_user(
    create_user: Annotated[
        schemes.CreateUser,
        Body(),
    ],
    session: Annotated[
        AsyncSession,
        Depends(database.get_scoped_session),
    ],
) -> JSONResponse:
    user: User = await crud.create_user(
        session=session,
        first_name=create_user.first_name,
        last_name=create_user.last_name,
    )
    return JSONResponse(
        content=schemes.User.from_model(user).model_dump(mode="json"),
        status_code=status.HTTP_201_CREATED,
    )
