FROM python:3.7.7

COPY . /app
WORKDIR /app

RUN apt-get update

RUN curl -fsSL https://deb.nodesource.com/setup_15.x | bash
RUN apt-get install -y nodejs
RUN npm install -g npm@latest
RUN npm install

# No .pyo and easier debugging
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -U pip
RUN pip install -r requirements.txt

# Needed to collectstatic
ENV SECRET_KEY secret
RUN ./manage.py collectstatic --noinput

RUN ./run.sh

ENV PORT 80

HEALTHCHECK --interval=5s \
            --timeout=5s \
             CMD curl -f http://127.0.0.1:$PORT || exit 1

# EXPOSE 443
EXPOSE 80

ENTRYPOINT run.sh

# ENTRYPOINT ["daphne", "-e", "ssl:443:privateKey=$KEY:certKey=$CERT", "django_project.asgi:application"]

# ENTRYPOINT ["daphne", "django_project.asgi:application", "--port", "80", "--bind", "website", "-v2"]
