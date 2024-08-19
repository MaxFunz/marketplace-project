# main.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# Добавьте этот маршрут для страницы авторизации
@app.get("/login", response_class=HTMLResponse)
async def login():
    return """
    <html>
        <body>
            <h2>Login Page</h2>
            <form method="post" action="/login">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username"><br><br>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password"><br><br>
                <input type="submit" value="Login">
            </form>
        </body>
    </html>
    """


DATABASE_URL = "postgresql+asyncpg://postgres:postgres@db:5432/mydatabase"
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
