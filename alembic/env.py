from __future__ import annotations
import asyncio
from logging.config import fileConfig

from sqlalchemy import create_engine, engine
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import sessionmaker

from alembic import context

from app.database import Base  # Замените на ваш путь

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:postgres@db:5432/mydatabase"

connectable = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

def run_migrations_online() -> None:
    async def run() -> None:
        async with connectable.connect() as connection:
            await connection.run_sync(Base.metadata.create_all)

    asyncio.run(run())
