FROM nginx:latest
      
WORKDIR /app
 
COPY backend/requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/app.py .
COPY backend/schema.sql .
COPY frontend /usr/share/nginx/html

EXPOSE 80

CMD  python -m gunicorn --bind 0.0.0.0:$PORT --workers 4 app:app && nginx -g "daemon off;"