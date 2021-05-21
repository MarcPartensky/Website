init:
	pip install pipenv
	pipenv install --dev
build:
	docker build . -t marcpartensky/website
push:
	docker push marcpartensky/website
up:
	docker-compose up -d
down:
	docker-compose down
run:
	./manage.py runserver 0.0.0.0:8000
makemigrations:
	./manage.py makemigrations
migrate:
	./manage.py migrate
shell:
	./manage.py shell
test:
	./manage.py runserver 0.0.0.0:8000 &
	curl localhost:8000
	kill %

