from http import HTTPStatus
from fastapi import APIRouter, Depends

from database.models import User
from schemas.response_schema import ResponseSchema
from schemas.user_schema import UserProfile
from utils.auth import get_current_user


router = APIRouter()

@router.get("/profile", response_model=ResponseSchema[UserProfile])
async def get_profile(current_user: User = Depends(get_current_user)):
    return ResponseSchema(
        status = HTTPStatus.FOUND.value,
        message = "Success get profile",
        data = current_user
    )