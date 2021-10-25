#!/bin/sh

echo -e 'Running \033[1mentrypoint.sh\033[0m'
./manage.py migrate
./manage.py createsuperuser --noinput
daphne django_project.asgi:application --port 80 --bind 127.0.0.1 -v2
