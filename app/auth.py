from fastapi import APIRouter, Depends, HTTPException, Form
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, schemas
from app.database import get_db
from app.email_producer import send_email_to_kafka

router = APIRouter()

@router.post("/register", response_class=HTMLResponse)
async def register(email: str = Form(...), password: str = Form(...), confirm_password: str = Form(...),
                   phone_number: str = Form(...), db: AsyncSession = Depends(get_db)):
    if password != confirm_password:
        return "Passwords do not match"

    user_data = schemas.UserCreate(email=email, password=password, confirm_password=confirm_password,
                                   phone_number=phone_number, name="")

    try:
        db_user = await crud.create_user(db=db, user=user_data)
        await send_email_to_kafka(email)  # Отправка в Kafka
        return "Registration successful"
    except ValueError as e:
        return str(e)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
