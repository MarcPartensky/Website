init:
	pip install pipenv
	pipenv install --dev
	npm install --save
update:
	pipenv lock --pre --clear
	npm update
activate:
	pipenv shell
deactivate:
	exit
build:
	./manage.py collectstatic
	docker build . -t marcpartensky/website
push:
	docker push marcpartensky/website
	git pushall
up:
	docker-compose up -d
down:
	docker-compose down
run:
	pipenv run ./manage.py runserver 127.0.0.1:8000
migrations:
	pipenv run ./manage.py makemigrations
migrate:
	pipenv run ./manage.py migrate
shell:
	pipenv run ./manage.py shell
brewstart:
	brew services start mysql
	brew services start redis
brewstop:
	brew services stop mysql
	brew services stop redis

