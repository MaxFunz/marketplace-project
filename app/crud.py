from sqlalchemy.ext.asyncio import AsyncSession
from app.models import User
from app.schemas import UserCreate
from passlib.context import CryptContext
from sqlalchemy.future import select

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def create_user(db: AsyncSession, user: UserCreate):
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

async def authenticate_user(db: AsyncSession, email: str, password: str):
    user = await get_user_by_email(db, email)
    if not user or not pwd_context.verify(password, user.hashed_password):
        return None
    return user

async def update_password(db: AsyncSession, user: User, new_password: str):
    user.hashed_password = pwd_context.hash(new_password)
    await db.commit()
    await db.refresh(user)
