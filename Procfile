web: daphne django_project.asgi:application --port $PORT --bind 0.0.0.0 -v2
ftp: ./manage.py ftpserver :21
redis: docker run -p 6379:6379 -d redis:5
worker: python manage.py runworker -v2
