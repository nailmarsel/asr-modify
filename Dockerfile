# Используем базовый образ Python
FROM python:3.9-slim

# Устанавливаем необходимые системные зависимости
RUN apt-get update && apt-get install -y ffmpeg

# Устанавливаем зависимости для Python
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы приложения в контейнер
COPY . /app

# Указываем команду для запуска приложения
CMD ["python", "main.py"]