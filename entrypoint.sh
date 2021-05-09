#!/bin/sh

./manage.py makemigrations
./manage.py migrate
daphne django_project.asgi:application --port 80 --bind website -v2
