FROM python:3.7-alpine

RUN apk update
RUN apk add git jpeg-dev zlib-dev libjpeg libffi-dev postgresql-dev gcc build-base python3-dev musl-dev

COPY requirements.txt /tmp
WORKDIR /tmp

RUN pip install -r requirements.txt

ENTRYPOINT ["gunicorn", "django_project.wsgi"]
