from asyncio import current_task
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)

from app.core.settings import settings

from .models import Model


class Database:
    engine: AsyncEngine
    session_factory: async_sessionmaker[AsyncSession]

    def __init__(self, url: str) -> None:
        self.engine = create_async_engine(
            url=url,
            echo=False,
        )

        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False,
        )

    async def get_scoped_session(
        self,
    ) -> AsyncGenerator[async_scoped_session[AsyncSession], None]:
        try:
            session: async_scoped_session[AsyncSession] = async_scoped_session(
                session_factory=self.session_factory,
                scopefunc=current_task,
            )
            yield session
        finally:
            await session.close()

    async def create_db(self) -> None:
        async with self.engine.begin() as connection:
            await connection.run_sync(Model.metadata.create_all)


database: Database = Database(
    url=settings.database.URL,
)
