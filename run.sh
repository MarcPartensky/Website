#!/bin/sh
/bin/sh .env

run_bg() {
	daphne -p $1 django_project.asgi:application > /dev/null &
}

mysql() {
	echo -e "Starting \e[92mMySQL\e[0m"
	docker-compose up -d mysql
}

redis() {
	echo -e "Starting \e[92mRedis\e[0m"
	docker-compose up -d redis
}

django() {
	echo -e "Starting \e[92mDjango\e[0m"
	# ./manage.py runserver 0.0.0.0:8000
	# daphne -p 8000 -b 0.0.0.0 django_project.asgi:application
	daphne -e "ssl:${PORT}:privateKey=${KEY}:certKey=${CERT}" django_project.asgi:application
}

alias run=django

up() {
	mysql
	redis
	django
}

down() {
	docker-compose down
	echo -e "Ended \e[31mRedis\e[0m"
	echo -e "Ended \e[31mMySQL\e[0m"
	kill % && echo -e "Ended \e[31mDjango\e[0m"	&& echo -e "Ended \e[31mFTP\e[0m"
}

ftp() {
	echo -e "Starting \e[92mFTP Server\e[0m"
	./manage.py ftpserver $FTP_URL
}

all() {
	ftp &
	up
	down
}


# build the project for docker
build() {
	./manage.py collectstatic --noinput
	docker build . -t marcpartensky/website
}

push() {
	./manage.py collectstatic --noinput
	docker build . -t marcpartensky/website
	docker push marcpartensky/website
	git push all
}

deploy() {
	./manage.py collectstatic --noinput
	./manage.py makemigrations
	./manage.py migrate
	run
}

update() {
	git pull
	pip install -U pip
	pip install -r requirements.txt -U
	npm update
}
