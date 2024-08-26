from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import User
from app.schemas import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def create_user(db: AsyncSession, user: UserCreate):
    existing_user = await get_user_by_email(db, user.email)
    if existing_user:
        raise ValueError("User already exists")

    hashed_password = pwd_context.hash(user.password)
    db_user = User(
        email=user.email,
        hashed_password=hashed_password,
        phone_number=user.phone_number,
        name=user.name
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).filter(User.email == email))
    return result.scalars().first()

async def get_user_by_id(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).filter(User.id == user_id))
    return result.scalars().first()

async def update_password(db: AsyncSession, user_id: int, new_password: str):
    user = await get_user_by_id(db, user_id)
    if user is None:
        raise ValueError("User not found")

    user.hashed_password = pwd_context.hash(new_password)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
