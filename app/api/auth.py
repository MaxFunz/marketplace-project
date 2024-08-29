from fastapi import APIRouter, Depends, HTTPException, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, schemas
from app.database import get_db
from app.email import send_email

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
        send_email(email, "Registration Successful", "You have successfully registered.")
        return RedirectResponse(url="/catalog", status_code=303)
    except ValueError as e:
        return str(e)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error: " + str(e))

@router.post("/login", response_class=HTMLResponse)
async def login(email: str = Form(...), password: str = Form(...), db: AsyncSession = Depends(get_db)):
    user = await crud.authenticate_user(db=db, email=email, password=password)
    if user:
        send_email(email, "Login Successful", "You have successfully logged in.")
        return RedirectResponse(url="/catalog", status_code=303)
    else:
        raise HTTPException(status_code=400, detail="Invalid credentials")

@router.post("/reset-password", response_class=HTMLResponse)
async def reset_password(email: str = Form(...), new_password: str = Form(...), db: AsyncSession = Depends(get_db)):
    try:
        await crud.reset_password(db=db, email=email, new_password=new_password)
        send_email(email, "Password Reset Successful", "Your password has been successfully reset.")
        return "Password reset successful"
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error: " + str(e))
