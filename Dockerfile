FROM python:3.10-slim

WORKDIR /app

COPY backend/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY backend/app.py ./
COPY backend/schema.sql ./


ENV PORT 8000

CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "app:app"]