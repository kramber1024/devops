import asyncio

import uvicorn
from fastapi import FastAPI

from app.api import api
from app.core.database import database

app: FastAPI = FastAPI(
    title="DevOps - API",
    root_path_in_servers=False,
)
app.include_router(api)


if __name__ == "__main__":
    asyncio.run(database.create_db())
    uvicorn.run(
        "app.__main__:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
