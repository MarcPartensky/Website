#!/bin/sh

port=${1:-$PORT}
host=${2:-$HOST}
port=${port:-"80"}
host=${addr:-"0.0.0.0"}
username=${DJANGO_SUPERUSER_USERNAME:-"admin"}
email=${DJANGO_SUPERUSER_EMAIL:-"admin@admin.com"}
DJANGO_SUPERUSER_PASSWORD=${PASSWORD:-$(date +%s | sha256sum | base64 | head -c 32)}

_kill() {
    kill $(cat /tmp/website.pid)
}

if [ $1 = "kill" ]; then
    _kill
    exit 0
fi

echo $$ > /tmp/website.pid

setup() {
    echo -e "Running \033[1mentrypoint.sh\033[0m using $HOST:$PORT"
    ./manage.py migrate
    echo -e "Creating \033[1msuper user\033[0m using:\n - username: \033[1m$username\033[0m\n - email: \033[1m$email\033[0m\n"
    ./manage.py createsuperuser --user $username --email $email --noinput
    ./manage.py collectstatic --noinput --clear
}

if [[ ! -z $NOSETUP && ! $1 = "--nosetup" ]]; then
    setup
fi

# dev vs prod
if [ -z $PRODUCTION ]; then
    daphne django_project.asgi:application --port $port --bind $host -v2
else
    ./manage.py runserver 127.0.0.1:8000
fi
