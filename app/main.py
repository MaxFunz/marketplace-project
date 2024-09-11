from fastapi.responses import HTMLResponse
from app.api import auth, user
from fastapi import FastAPI, BackgroundTasks
from app.my_email import send_email_async
app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(user.router, prefix="/user", tags=["user"])

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <body>
            <h1>Welcome to the Registration System</h1>
            <a href="/auth/register">Register</a><br>
            <a href="/auth/login">Login</a><br>
            <a href="/auth/reset-password">Reset Password</a>
        </body>
    </html>
    """

@app.get("/catalog", response_class=HTMLResponse)
async def catalog_page():
    return """
    <html>
        <body>
            <h1>Catalog Page</h1>
            <p>Welcome to the catalog!</p>
        </body>
    </html>
    """
@app.post("/register/")
async def register_user(email: str, background_tasks: BackgroundTasks):
    # Пример вызова функции отправки email
    await send_email_async('Успешная регистрация!', 'Вы успешно зарегистрировались на сайте!', email, background_tasks)
    return {"message": "Регистрация успешна, проверьте вашу почту для подтверждения!"}