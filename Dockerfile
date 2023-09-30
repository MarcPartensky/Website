FROM python:3.7.17-alpine as builder

# Pre installations
RUN apk update
RUN apk add --update --virtual .tmp libffi-dev build-base linux-headers
RUN apk add curl jpeg-dev zlib-dev npm
RUN pip install poetry

# Copy useful files
WORKDIR /opt/website
COPY pyproject.toml poetry.lock package.json package-lock.json ./

# Run updates
RUN poetry update
RUN poetry export -f requirements.txt --without-hashes --output requirements.txt
RUN npm update
RUN npm install

# Image of production
FROM python:3.7.17-alpine
# FROM alpine
ENV SECRET_KEY=whatever
# ARG timestamp
# ARG commit
# LABEL build.timestamp=timestamp
# LABEL build.commit=commit

# Labels
LABEL maintainer="marc.partensky@gmail.com"
LABEL image="https://hub.docker.com/r/marcpartensky/website"
LABEL source="https://github.com/marcpartensky/website"
LABEL link="https://marcpartensky.com"

# Install curl and stuff for pillow
RUN apk update
RUN apk add --update --virtual .tmp libffi-dev build-base linux-headers
RUN apk add python3 curl jpeg-dev zlib-dev py3-pip
RUN apk add shadow

# Setup home user website
RUN useradd -m website
USER website

# Copy useful files
WORKDIR /home/website
COPY --chown=website website ./website
COPY --chown=website --from=builder /opt/website/requirements.txt ./
COPY LICENSE ./

# No .pyo and easier debugging
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
# RUN pip install -U pip
RUN pip install -r requirements.txt
RUN ./website/manage.py makemigrations
RUN ./website/manage.py collectstatic --noinput

USER root
RUN apk del .tmp
USER website

# Setup env vars for entrypoint.sh
ENV PORT 80
ENV HOST 0.0.0.0
ENV PATH="${PATH}:/home/website/.local/bin"
EXPOSE 80

# Check health
HEALTHCHECK --interval=30s \
            --timeout=10s \
            --start-period=1m \
            --retries=3 \
             CMD curl -sSf http://localhost:$PORT/live || exit 1

WORKDIR /home/website/website
ENTRYPOINT ["./entrypoint.sh"]
# ENTRYPOINT ["daphne", "-e", "ssl:443:privateKey=$KEY:certKey=$CERT", "django_project.asgi:application"]
