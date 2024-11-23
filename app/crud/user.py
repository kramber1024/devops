from typing import TYPE_CHECKING

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database.models import User

if TYPE_CHECKING:
    from sqlalchemy import Result


async def create_user(
    *,
    session: AsyncSession,
    first_name: str,
    last_name: str,
) -> User:
    user: User = User(
        first_name=first_name,
        last_name=last_name,
    )

    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def get_users_all(
    *,
    session: AsyncSession,
) -> list[User]:
    result: Result[tuple[User]] = await session.execute(
        select(User),
    )
    users: list[User] = list(result.scalars().all())

    return users
