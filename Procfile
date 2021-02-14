web: daphne django_project.asgi:application --port $PORT --bind 0.0.0.0 -v2
channels: python manage.py runworker channels -v2
ftp: ./manage.py ftpserver :21
redis: docker run -p 6379:6379 -d redis:5
release: ./manage.py makemigrations ./manage.py migrate
migrate: ./manage.py migrate
makemigrations: ./manage.py makemigrations
