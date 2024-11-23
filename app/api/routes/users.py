from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router: APIRouter = APIRouter(
    prefix="/users",
)


@router.get("/")
def get_users() -> JSONResponse:
    return JSONResponse(
        content={"message": "GET users"}, status_code=status.HTTP_200_OK
    )
