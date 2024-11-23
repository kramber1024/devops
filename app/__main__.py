import uvicorn
from fastapi import FastAPI

from app.api import api

app: FastAPI = FastAPI(
    title="DevOps - API",
    root_path_in_servers=False,
)
app.include_router(api)

if __name__ == "__main__":
    uvicorn.run(
        "app.__main__:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
