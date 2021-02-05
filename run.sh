trap 'kill $BGPID; exit' INT
# background command
echo -e "Starting \e[33mDjango"
daphne -p 80 django_project.asgi:application &
BGPID=$!
# foreground command of the script
echo -e "Starting \e[32mFtp Server"
./manage.py ftpserver 127.0.0.1:10021