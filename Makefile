# HOST := localhost
# PORT := 8000
PRODUCTION := false

.PHONY: start list build push setup update init test up down migrate brewstart brewstop dev prod clean deploy

start:
	pipenv run ./entrypoint.sh --nosetup
list:
	@LC_ALL=C $(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'
build: update
	docker-compose -f dev.yml build website
push: build
	git pushall
	docker-compose -f dev.yml push website
setup: init update start
update:
	npm update
	npm audit fix || echo npm audit fix failed
	# pipenv lock --pre --clear
	pipenv update
	pipenv lock -r > requirements.txt
	SECRET_KEY=secret pipenv run ./manage.py collectstatic --noinput
	SECRET_KEY=secret pipenv run ./manage.py makemigrations
init: .env
	pip install --user pipenv
	pipenv install --dev
	npm install --save
test:
	pipenv run ./manage.py test
kill:
	pipenv run ./entrypoint.sh kill
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
.env:
	echo HOST=localhost > .env
	echo PORT=8000 >> .env
	echo PRODUCTION=false >> .env
	echo NOSETUP=true >> .env
	echo SECRET=$$(date +%s | sha256sum | base64 | head -c 32 && echo) >> .env
