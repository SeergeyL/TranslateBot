FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY /app /app
COPY .env /app

CMD ["python3", "main.py"]
