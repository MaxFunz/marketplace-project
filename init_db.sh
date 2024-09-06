#!/bin/bash
# Применяем миграции
alembic upgrade head

# Запускаем приложение
exec "$@"
