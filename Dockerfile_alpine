FROM python:3.7-alpine

RUN apk update
RUN apk add git jpeg-dev zlib-dev libjpeg libffi-dev postgresql-dev gcc build-base python3-dev musl-dev

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .
WORKDIR .

EXPOSE 8000
EXPOSE 10021

ENTRYPOINT ["./run.sh"]
