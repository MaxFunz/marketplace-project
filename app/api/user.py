from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, schemas
from app.database import get_db
from app.dependencies import oauth2_scheme

router = APIRouter()

@router.post("/register", response_model=schemas.UserResponse)
async def register_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    pass

@router.post("/users/", response_model=schemas.UserResponse)
async def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    if user.password != user.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")
    user_data = await crud.create_user(db, user)
    return user_data

@router.get("/profile", response_model=schemas.UserResponse)
async def read_users_me(db: AsyncSession = Depends(get_db), token: str = Depends(oauth2_scheme)):
    user = await crud.get_user_by_email(db, token)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user