#!/bin/sh

port=${1:-$PORT}
addr=${2:-$ADDR}
port=${port:-"80"}
addr=${addr:-"127.0.0.1"}
username=${USERNAME:-"admin"}
email=${EMAIL:-"admin@admin.com"}
DJANGO_SUPERUSER_PASSWORD=${PASSWORD:-$(date +%s | sha256sum | base64 | head -c 32)}

echo -e "Running \033[1mentrypoint.sh\033[0m using $ADDR:$PORT"
./manage.py migrate
echo -e "Creating \033[1msuper user\033[0m using:\n - username: \033[1m$username\033[0m\n - email: \033[1m$email\033[0m\n"
./manage.py createsuperuser --user $username --email $email --noinput
./manage.py collecstatic --noinput
daphne django_project.asgi:application --port $port --bind $addr -v2
