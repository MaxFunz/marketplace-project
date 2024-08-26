from fastapi import APIRouter, Query
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/catalog", response_class=HTMLResponse)
async def catalog_page(page: int = Query(1, ge=1), db: AsyncSession = Depends(get_db)):
    items_per_page = 10
    offset = (page - 1) * items_per_page

    # Тут должна быть логика получения товаров из базы данных
    # Например, использование модели `Product` для запроса товаров с пагинацией

    return f"""
    <html>
        <body>
            <h1>Catalog Page</h1>
            <p>Welcome to the catalog!</p>
            <a href="/catalog?page={page - 1}" {'disabled' if page == 1 else ''}>Previous</a>
            <a href="/catalog?page={page + 1}">Next</a>
        </body>
    </html>
    """
