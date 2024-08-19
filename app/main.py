from fastapi import FastAPI
from app.models import Base, User
from app.db import engine, async_session

app = FastAPI()

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("startup")
async def on_startup():
    await init_db()

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    async with async_session() as session:
        result = await session.execute(select(User).where(User.id == user_id))
        user = result.scalars().first()
        return user
