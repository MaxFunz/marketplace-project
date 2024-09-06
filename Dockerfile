FROM python:3.9-slim

# Установите рабочую директорию
WORKDIR /app

# Копируйте файлы проекта
COPY . /app

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Сделайте скрипт инициализации исполняемым
RUN chmod +x /app/init_db.sh

# Команда по умолчанию
CMD ["/app/init_db.sh", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
