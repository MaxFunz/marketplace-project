from pydantic import BaseModel, EmailStr, constr
from typing import Optional


class UserCreate(BaseModel):
   email: EmailStr
   password: constr(min_length=6)
   confirm_password: constr(min_length=6)
   phone_number: Optional[str] = None
   name: str


   class Config:
       schema_extra = {
           "example": {
               "email": "user@example.com",
               "password": "yourpassword",
               "confirm_password": "yourpassword",
               "phone_number": "+1234567890",
               "name": "John Doe"
           }
       }


class UserResponse(BaseModel):
   email: EmailStr
   phone_number: Optional[str] = None
   name: str


   class Config:
       schema_extra = {
           "example": {
               "email": "user@example.com",
               "phone_number": "+1234567890",
               "name": "John Doe"
           }
       }
