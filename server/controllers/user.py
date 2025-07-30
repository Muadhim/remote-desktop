from fastapi import APIRouter, Depends

from database.models import User
from schemas.user import UserProfile
from utils.auth import get_current_user


router = APIRouter()

@router.get("/profile", response_model=UserProfile)
async def get_profile(current_user: User = Depends(get_current_user)):
    return current_user