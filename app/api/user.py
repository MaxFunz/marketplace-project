from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, schemas
from app.database import get_db
from app.dependencies import oauth2_scheme
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/profile", response_model=schemas.UserResponse)
async def read_users_me(db: AsyncSession = Depends(get_db), token: str = Depends(oauth2_scheme)):
    user = await crud.get_user_by_email(db, token)  # В реальном приложении нужно декодировать JWT токен
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/catalog", response_class=HTMLResponse)
async def catalog_page(page: int = 1, db: AsyncSession = Depends(get_db)):
    per_page = 10
    # Для демонстрации: мы используем простую страницу без реальных данных
    # Для реального использования нужно добавить модели и запросы для получения данных о товарах
    return f"""
    <html>
        <body>
            <h1>Catalog Page</h1>
            <p>Displaying page {page} of catalog.</p>
            <a href="/catalog?page={page-1}">Previous</a> | <a href="/catalog?page={page+1}">Next</a>
        </body>
    </html>
    """
