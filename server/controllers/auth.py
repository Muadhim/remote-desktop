from datetime import timedelta
from email import message
from http import HTTPStatus
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from database import get_db
from database.models import User
from schemas.response_schema import ResponseSchema
from schemas.user_schema import Token, UserCreate, UserLogin, UserResponse
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession

from utils.auth import create_access_token, verify_password


router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

@router.post("/register", response_model=ResponseSchema[UserResponse])
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == user.email))
    existing_user = result.scalars().first()

    if existing_user:
        return ResponseSchema(
            status=HTTPStatus.BAD_REQUEST.value,
            message="Email already registered",
            data=None
        )
    
    hashed_password = pwd_context.hash(user.password)
    new_user = User(email=user.email, username=user.username, password=hashed_password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return ResponseSchema(
        status=HTTPStatus.CREATED.value,
        message="Success to register",
        data=new_user
    )


@router.post("/login", response_model=Token)
async def login(user: UserLogin, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.username == user.username))
    db_user = result.scalars().first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(data={"sub": db_user.username},
                                expires_delta=timedelta(minutes=60))
    return {"access_token": token, "token_type": "bearer"}