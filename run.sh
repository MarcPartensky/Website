trap 'kill $BGPID; exit' INT
# background command
echo -e "Starting \e[33mDjango"
gunicorn --bind 127.0.0.1:8000 django_project.wsgi &
BGPID=$!
# foreground command of the script
echo -e "Starting \e[32mFtp Server"
./manage.py ftpserver 127.0.0.1:10021
