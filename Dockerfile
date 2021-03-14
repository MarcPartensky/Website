FROM python:3.7.7

RUN apt-get update

# No .pyo
ENV PYTHONDONTWRITEBYTECODE 1
# Easier debugging
ENV PYTHONUNBUFFERED 1

COPY . /app
WORKDIR /app

RUN pip install -U pip
RUN pip install -r requirements.txt

# RUN ./manage.py makemigrations
# RUN ./manage.py migrate
# RUN ./manage.py collectstatic --noinput

# EXPOSE 443
# RUN /app/run.sh

# ENTRYPOINT ["daphne", "django_project.asgi:application", "--port", "8000", "--bind", "0.0.0.0", "-v2"]
# ENTRYPOINT ["daphne", "-e", "ssl:443:privateKey=privkey.pem:certKey=fullchain.pem", "django_project.asgi:application"]
ENTRYPOINT ["daphne", "-e", "ssl:443:privateKey=$KEY:certKey=$CERT", "django_project.asgi:application"]
