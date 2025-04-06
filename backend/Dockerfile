FROM python:3.11.9-slim

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Сначала запускаем models.py, затем main.py и запускаем сервер
CMD python models.py && python main.py && uvicorn main:app --host 0.0.0.0 --port 8000
