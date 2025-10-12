# Multi-stage build for production
FROM python:3.11-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python manage.py collectstatic --noinput || true

CMD ["gunicorn", "social_media_api.wsgi:application", "--bind", "0.0.0.0:8000"]
