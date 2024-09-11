FROM python:3.9-slim

# Установите рабочую директорию
WORKDIR /app

# Копируйте файлы проекта
COPY . /app

# Установите зависимости
RUN pip install --upgrade pip

RUN pip install -r requirements.txt