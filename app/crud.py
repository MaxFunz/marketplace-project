from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(
        email=user.email,
        hashed_password=hashed_password,
        phone_number=user.phone_number,
        name=user.name
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
