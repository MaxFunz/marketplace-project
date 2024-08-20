from fastapi import APIRouter, Depends, HTTPException, Form
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, schemas, email
from app.database import get_db
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.get("/register", response_class=HTMLResponse)
async def get_register_page():
    return """
    <html>
        <body>
            <h1>Register</h1>
            <form action="/auth/register" method="post">
                Email: <input type="email" name="email"><br>
                Password: <input type="password" name="password"><br>
                Confirm Password: <input type="password" name="confirm_password"><br>
                Phone Number: <input type="text" name="phone_number"><br>
                <input type="submit" value="Register">
            </form>
        </body>
    </html>
    """


@router.post("/register", response_class=HTMLResponse)
async def register(email: str = Form(...), password: str = Form(...), confirm_password: str = Form(...),
                   phone_number: str = Form(...), db: AsyncSession = Depends(get_db)):
    if password != confirm_password:
        return "Passwords do not match"

    user_data = schemas.UserCreate(email=email, password=password, confirm_password=confirm_password,
                                   phone_number=phone_number, name="")

    try:
        db_user = await crud.create_user(db=db, user=user_data)
        await email.send_email(to_email=email, subject="Registration successful",
                               body="You have successfully registered.")
        return "Registration successful"
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
