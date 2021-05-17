init:
	pip install pipenv
	pipenv install --dev
run:
	./manage.py runserver
shell:
	./manage.py shell
test:
	./manage.py runserver localhost:8000 &
	curl localhost:8000
	kill %

