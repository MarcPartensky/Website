# Website

This is the code of my personal website.
[https://websiteofmarcpartensky.herokuapp.com/](https://websiteofmarcpartensky.herokuapp.com/)

## Light theme
[![light theme](https://cdn.discordapp.com/attachments/702863598761803806/782335262499930112/light.png)](https://websiteofmarcpartensky.herokuapp.com)

## Dark theme
[![dark theme](https://cdn.discordapp.com/attachments/702863598761803806/782334455385555014/dark.png)](https://websiteofmarcpartensky.herokuapp.com?theme=dark)

## Install

### From [source](https://github.com/MarcPartensky/Website) (requires [git](https://git-scm.com/), [python](https://www.python.org/), [pip](https://pip.pypa.io/en/stable/installing/))
```sh
git clone https://github.com/marcpartensky/website
pip install -r requirements.txt
gunicorn django_project.wsgi
```
## Deploy

### With [Docker](docker.com)
> Build : > 10 minutes
```sh
docker run -it -e SECRET_KEY=[RANDOMSTRING] -p 8000:8000 marcpartensky/website
```
### Or
```sh
git clone https://github.com/marcpartensky/website
cd website
docker-compose up
```

> If you’re using Docker natively on Linux, Docker Desktop for Mac, or Docker Desktop for Windows, then the web app should now be listening on port 8000 on your Docker daemon host. Point your web browser to http://localhost:8000 to find the Hello World message. If this doesn’t resolve, you can also try http://127.0.0.1:8000.

> If you’re using Docker Machine on a Mac or Windows, use docker-machine ip MACHINE_VM to get the IP address of your Docker host. Then, open http://MACHINE_VM_IP:8000 in a browser.

From https://docs.docker.com/compose/gettingstarted/

## Add me as a contact
![qrcode](./static/qrcode.svg)
**Scan to add me as a contact**

## Useful links
https://docs.docker.com/compose/gettingstarted/

