FROM python:alpine
WORKDIR /app
COPY . .
ENV DJANGO_SUPERUSER_PASSWORD='.'
RUN pip install djangorestframework django-environ uvicorn pygments && \
    python manage.py makemigrations app && \
    python manage.py migrate && \
    python manage.py createsuperuser --noinput --username o --email o@o.com && \
    python manage.py collectstatic --noinput