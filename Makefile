init:
	pip install pipenv
	pipenv install --dev
	npm install --save
build:
	npm update
	npm audit fix
	pipenv lock --pre --clear
	pipenv run ./manage.py collectstatic
	pipenv run ./manage.py makemigrations
	docker build . -t marcpartensky/website
	docker push marcpartensky/website
	git pushall
up:
	docker-compose up -d
down:
	docker-compose -f dev.yml down
	docker-compose -f docker-compose.yml down
	DOCKER_HOST=ssh://vps docker-compose -f dev.ym up -d --build --force-recreate --remove-orphans website-test
run:
	pipenv run ./manage.py runserver 127.0.0.1:8000
migrate:
	pipenv run ./manage.py migrate
brewstart:
	brew services start mysql
	brew services start redis
brewstop:
	brew services stop mysql
	brew services stop redis
dev:
	docker-compose -f dev.yml up -d
devlogs:
	docker-compose -f dev.yml logs -f
prod:
	docker-compose -f docker.compose.yml up -d
clean:
	docker-compose -f docker-compose.yml down
	docker-compose -f dev.yml down
deploy:
	DOCKER_HOST=ssh://vps docker-compose -f dev.yml up -d --build --force-recreate --remove-orphans website-test
	DOCKER_HOST=ssh://vps docker-compose -f docker-compose.dev.ym logs -f website-test
