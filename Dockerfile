FROM python:3.7.12
# ARG timestamp
# ARG commit
LABEL maintainer="marc.partensky@gmail.com"
LABEL image="https://hub.docker.com/r/marcpartensky/website"
LABEL source="https://github.com/marcpartensky/website"
LABEL link="https://marcpartensky.com"
# LABEL build.timestamp=timestamp
# LABEL build.commit=commit

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
ENV HOST 0.0.0.0
EXPOSE 80
# EXPOSE 443

HEALTHCHECK --interval=30s \
            --timeout=10s \
            --start-period=1m \
            --retries=3 \
             CMD curl -sSf http://127.0.0.1:$PORT/live || exit 1

ENTRYPOINT ["/app/entrypoint.sh"]
# ENTRYPOINT ["daphne", "-e", "ssl:443:privateKey=$KEY:certKey=$CERT", "django_project.asgi:application"]
