FROM python:3.10-slim

WORKDIR /app

COPY backend/requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/app.py ./
COPY backend/schema.sql ./

CMD ["python", "-m", "gunicorn", "--bind", "0.0.0.0:8080", "app:app"]