#!/bin/sh
source .env

run_bg() {
	pipenv run daphne -p $1 django_project.asgi:application > /dev/null &
}

mysql() {
	echo -e "Starting \e[92mMySQL\e[0m"
	docker-compose up -d mysql
}

postgres() {
	echo -e "Starting \e[92mPostgreSQL\e[0m"
	docker-compose up -d postgres
}

redis() {
	echo -e "Starting \e[92mRedis\e[0m"
	docker-compose up -d redis
}

django() {
	echo -e "Starting \e[92mDjango\e[0m"
	# ./manage.py runserver 0.0.0.0:8000
	# daphne -p 8000 -b 0.0.0.0 django_project.asgi:application
	pipenv run daphne -e "ssl:${PORT}:privateKey=${KEY}:certKey=${CERT}" django_project.asgi:application
}

ftp() {
	echo -e "Starting \e[92mFTP Server\e[0m"
	pipenv run ./manage.py ftpserver $FTP_URL
}

all() {
	ftp &
	up
	down
}


# build the project for docker
build() {
	pipenv run ./manage.py collectstatic --noinput
	docker build . -t marcpartensky/website
	docker push marcpartensky/website
	git pull --all
	git push -ll
}

deploy() {
	pipenv run ./manage.py collectstatic --noinput
	pipenv run ./manage.py makemigrations
	pipenv run ./manage.py migrate
	run
}

updatepip() {
	git pull
	pipenv run pip install -U pip
	pipenv run pip install -r requirements.txt -U
	npm update
}

lock() {
	pipenv lock --pre --clear
}
