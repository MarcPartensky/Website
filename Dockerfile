FROM python:3.7.7

COPY . /app
WORKDIR /app

RUN apt-get update

RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash
RUN apt-get install -y nodejs
RUN npm install -g npm@latest
RUN npm install

# No .pyo and easier debugging
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -U pip
RUN pip install -r requirements.txt

ENV PORT 80
EXPOSE 80
# EXPOSE 443

HEALTHCHECK --interval=5s \
            --timeout=5s \
             CMD curl -sf http://127.0.0.1:$PORT/robots.txt || exit 1

ENTRYPOINT entrypoint.sh

# ENTRYPOINT ["daphne", "-e", "ssl:443:privateKey=$KEY:certKey=$CERT", "django_project.asgi:application"]
