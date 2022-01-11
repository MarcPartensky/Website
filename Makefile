start:
	pipenv run ./manage.py runserver 127.0.0.1:8000
build: update
	docker build . -t marcpartensky/website
push: build
	git pushall
	docker push marcpartensky/website
setup: install update start
update:
	npm update
	npm audit fix
	pipenv lock --pre --clear
	pipenv lock -r > requirements.txt
	pipenv run ./manage.py collectstatic --noinput
	pipenv run ./manage.py makemigrations
install:
	pip install --user pipenv
	pipenv install --dev
	npm install --save
up: init
	docker-compose up -d
down:
	docker-compose -f dev.yml down
	docker-compose -f docker-compose.yml down
	DOCKER_HOST=ssh://vps docker-compose -f dev.ym up -d --build --force-recreate --remove-orphans website-test
migrate: update
	pipenv run ./manage.py migrate
brewstart:
	brew services start mysql
	brew services start redis
brewstop:
	brew services stop mysql
	brew services stop redis
dev:
	docker-compose -f dev.yml up -d --build --remove-orphans
	exec docker-compose -f dev.yml logs -f
prod:
	docker-compose -f docker-compose.yml up -d --build --remove-orphans
clean:
	docker-compose -f docker-compose.yml down
	docker-compose -f dev.yml down
deploy:
	DOCKER_HOST=ssh://vps docker-compose -f dev.yml up -d --build --force-recreate --remove-orphans website-test
	DOCKER_HOST=ssh://vps docker-compose -f docker-compose.dev.ym logs -f website-test
