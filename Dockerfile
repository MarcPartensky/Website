FROM python:3.7-alpine

RUN apk update
RUN apk add git jpeg-dev zlib-dev libjpeg libffi-dev postgresql-dev gcc build-base python3-dev musl-dev

COPY requirements.txt /

RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app
EXPOSE 8000

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000", "django_project.wsgi"]
