# Используем базовый образ Python
FROM python:3.9-slim

# Устанавливаем необходимые системные зависимости
RUN apt-get update && apt-get install -y ffmpeg

# Устанавливаем зависимости для Python
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install --no-cache-dir -r requirements.txt

# Устанавливаем PyTorch
RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113

# Копируем скрипт для загрузки модели и выполняем его
COPY download_model.py /app/download_model.py
RUN mkdir -p /app/models/whisper
RUN python3 /app/download_model.py

RUN ls -l /app/models/whisper/
# Копируем все файлы приложения в контейнер
COPY . /app

# Указываем команду для запуска приложения
ENTRYPOINT ["python3", "main.py"]