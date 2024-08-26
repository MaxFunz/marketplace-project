from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.api import auth, user

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
