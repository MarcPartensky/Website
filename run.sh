#!/bin/sh

run_with_ssl() {
	"daphne -e ssl:443:privateKey=$KEY:certKey=$CERT django_project.asgi:application"
}

run() {
	daphne -p $1 django_project.asgi:application > /dev/null &
}

mysql() {
	source .env
	docker-compose up -d mysql
}

redis() {
	source .env
	docker-compose up -d redis
}

django() {
	source .env
	echo -e "Starting \e[33mDjango\e[0m"
	# ./manage.py runserver 0.0.0.0:8000
	export REDIS_URL="localhost:6379"
	daphne -p 8000 -b 0.0.0.0 django_project.asgi:application
}

up() {
	mysql
	redis
	django
}

down() {
	docker-compose down
	kill %
}

ftp() {
	./manage.py ftpserver 127.0.0.1:10021
}

run_all() {
	trap 'kill $BGPID; exit' INT
	# background command
	echo -e "Starting \e[33mDjango\e[0m"
	daphne -p 80 django_project.asgi:application &
	BGPID=$!
	# foreground command of the script
	echo -e "Starting \e[32mFtp Server"
	./manage.py ftpserver 127.0.0.1:10021
}
