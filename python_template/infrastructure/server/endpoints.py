from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/hello")
async def hello():
    return "Hello!"
