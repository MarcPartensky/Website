FROM python:3.7.12-alpine as builder
WORKDIR /opt/website
COPY website /opt/website/website
COPY package.json package-lock.json ./

RUN apk add curl npm gcc

RUN pip install poetry
RUN poetry update
RUN npm install

FROM python:3.7.12-alpine
# ARG timestamp
# ARG commit
LABEL maintainer="marc.partensky@gmail.com"
LABEL image="https://hub.docker.com/r/marcpartensky/website"
LABEL source="https://github.com/marcpartensky/website"
LABEL link="https://marcpartensky.com"
# LABEL build.timestamp=timestamp
# LABEL build.commit=commit

COPY --from=builder /opt/website /opt/website
WORKDIR /opt/website

RUN apk update
RUN apk add curl npm

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

ENTRYPOINT ["./entrypoint.sh"]
# ENTRYPOINT ["daphne", "-e", "ssl:443:privateKey=$KEY:certKey=$CERT", "django_project.asgi:application"]
