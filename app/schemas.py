from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    confirm_password: str
    phone_number: str
    name: str

class UserResponse(BaseModel):
    email: EmailStr
    name: str

    class Config:
        orm_mode = True
