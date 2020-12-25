web: gunicorn django_project.wsgi
worker: ./manage.py ftpserver 0.0.0.0:21
worker: docker run -p 6379:6379 -d redis:5
