FROM python:3.7.3

RUN apt update
# RUN apk add git jpeg-dev zlib-dev libjpeg libffi-dev postgresql-dev gcc build-base python3-dev musl-dev

COPY . .
WORKDIR .

RUN pip install -U pip
RUN pip install -r requirements.txt
RUN chmod +x /django_project/asgi.py

RUN ./manage.py makemigrations
RUN ./manage.py migrate
RUN ./manage.py collectstatic --noinput

# EXPOSE 8000
# EXPOSE 10021
# EXPOSE 80
EXPOSE 443

# ENTRYPOINT ["./run.sh"]
# ENTRYPOINT ["daphne", "django_project.asgi:application", "--port", "8000", "--bind", "0.0.0.0", "-v2"]
# daphne -e ssl:443:privateKey=/etc/letsencrypt/live/marcpartensky.com/privkey.pem:certKey=/etc/letsencrypt/live/marcpartensky.com/fullchain.pem django_project.asgi:application
# daphne -e ssl:443:privateKey=key.pem:certKey=crt.pem django_project.asgi:application

# ENTRYPOINT ["daphne", "-e", "ssl:443:privateKey=${KEY}:certKey=${CERT}", "django_project.asgi:application"]
ENTRYPOINT ["daphne", "-e", "ssl:443:privateKey=key.pem:certKey=cert.pem", "django_project.asgi:application"]
