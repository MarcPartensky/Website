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
	docker build . -t marcpartensky/website
push:
	docker push marcpartensky/website
	git pushall
up:
	docker-compose up -d
down:
	docker-compose down
run:
	pipenv run ./manage.py runserver 0.0.0.0:8000
migrations:
	pipenv run ./manage.py makemigrations
migrate:
	pipenv run ./manage.py migrate
shell:
	pipenv run ./manage.py shell
test:
	pipenv run ./manage.py runserver 0.0.0.0:8000 &
	curl localhost:8000
	kill %
brew:
	brew services start postgresql
	brew services start redis
