init:
	pip install pipenv
	pipenv install --dev
build:
	docker build . -t marcpartensky/website
push:
	docker push marcpartensky/website
run:
	./manage.py runserver
shell:
	./manage.py shell
test:
	./manage.py runserver localhost:8000 &
	curl localhost:8000
	kill %

