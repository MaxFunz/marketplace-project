from fastapi import APIRouter, Depends, HTTPException, Form
from fastapi.responses import HTMLResponse
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
        await send_email(email, "Registration successful", "You have successfully registered.")
        return """
        <html>
            <body>
                <h1>Registration successful</h1>
                <p>Check your email for confirmation.</p>
                <a href="/catalog">Go to catalog</a>
            </body>
        </html>
        """
    except ValueError as e:
        return str(e)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login", response_class=HTMLResponse)
async def login(email: str = Form(...), password: str = Form(...), db: AsyncSession = Depends(get_db)):
    user = await crud.get_user_by_email(db, email)
    if not user or not crud.pwd_context.verify(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    return """
    <html>
        <body>
            <h1>Login successful</h1>
            <a href="/catalog">Go to catalog</a>
        </body>
    </html>
    """


@router.post("/reset-password", response_class=HTMLResponse)
async def reset_password(email: str = Form(...), new_password: str = Form(...),
                         db: AsyncSession = Depends(get_db)):
    user = await crud.get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    try:
        await crud.update_password(db, user.id, new_password)
        await send_email(email, "Password reset successful", "Your password has been updated.")
        return """
        <html>
            <body>
                <h1>Password reset successful</h1>
                <a href="/auth/login">Login</a>
            </body>
        </html>
        """
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
