FROM python:3.7.3

RUN apt update
# RUN apk add git jpeg-dev zlib-dev libjpeg libffi-dev postgresql-dev gcc build-base python3-dev musl-dev

# No pyo
ENV PYTHONDONTWRITEBYTECODE 1
# Easier debugging
ENV PYTHONUNBUFFERED 1

COPY . .
WORKDIR .

RUN pip install -U pip
RUN pip install -r requirements.txt
# RUN chmod +x /django_project/asgi.py

RUN ./manage.py makemigrations
RUN ./manage.py migrate
RUN ./manage.py collectstatic --noinput


EXPOSE 443
# EXPOSE 8000
# EXPOSE  40000-50000
# EXPOSE 10021

# ENTRYPOINT ["daphne", "django_project.asgi:application", "--port", "8000", "--bind", "0.0.0.0", "-v2"]
ENTRYPOINT ["daphne", "-e", "ssl:443:privateKey=key.pem:certKey=cert.pem", "django_project.asgi:application"]
