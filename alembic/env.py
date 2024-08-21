from sqlalchemy import create_engine, pool
from alembic import context
from logging.config import fileConfig
from sqlalchemy.engine import Connection

# Импортируйте ваши модели здесь
from app.models import Base

# Эта строка извлекает конфигурацию из файла alembic.ini
config = context.config

# Настройка логирования из файла конфигурации
fileConfig(config.config_file_name)

# Метаданные из моделей
target_metadata = Base.metadata

def run_migrations_offline():
    """Запуск миграций в режиме 'offline'."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Запуск миграций в режиме 'online'."""
    # Используем синхронный движок
    connectable = create_engine(
        config.get_main_option("sqlalchemy.url"),
        poolclass=pool.NullPool
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
