FROM python:3.9-slim

# Установите рабочую директорию
WORKDIR /app

# Копируйте файлы проекта
COPY . /app

RUN pip install --upgrade pip
# Установите зависимости
RUN pip install -r requirements.txt
