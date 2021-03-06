author: Marc Partensky
name: Website of Marc Partensky
date: 8/10/2019
---

[![ViewCount](http://hits.dwyl.com/MarcPartensky/website.svg)](https://github.com/MarcPartensky/Website)

# Website

This is the code of my personal website.
[https://marcpartensky.com/](https://marcpartensky.com/)

## Light theme
[![light theme](https://cdn.discordapp.com/attachments/702863598761803806/782335262499930112/light.png)](https://websiteofmarcpartensky.herokuapp.com)

## Dark theme
[![dark theme](https://cdn.discordapp.com/attachments/702863598761803806/782334455385555014/dark.png)](https://websiteofmarcpartensky.herokuapp.com?theme=dark)

## Install

### From [source](https://github.com/MarcPartensky/Website) (requires [git](https://git-scm.com/), [python](https://www.python.org/), [pip](https://pip.pypa.io/en/stable/installing/))
```sh
git clone https://github.com/marcpartensky/website
```

```sh
pip install -r requirements.txt
# or with pipenv (recommended, install pipenv with pip install pipenv)
pipenv install
```

```sh
./manage.py runserver
```

## Deploy with [Docker](docker.com)

### Run website as standalone 

#### run unsecured for quick test
```sh
docker run -it \
	-e SECRET_KEY=$(openssl rand -base64 32) \
	-p 80:80 \
	marcpartensky/website
	./manage.py runserver
```

#### or run with ssl certificate
```sh
docker run -it \
	-env CERT \ # You must export a ssl certificate path
	-env KEY \ # You must export a pem key path
	-e SECRET_KEY=$(openssl rand -base64 32) \
	-p 443:443 \
	marcpartensky/website
```

### Or run with middleware (databases)
```sh
git clone https://github.com/marcpartensky/website
cd website
docker-compose up
```

> If you’re using Docker natively on Linux, Docker Desktop for Mac, or Docker Desktop for Windows, then the web app should now be listening on port 443 on your Docker daemon host. Point your web browser to http://localhost:443 to find the Hello World message. If this doesn’t resolve, you can also try http://127.0.0.1:443.

From https://docs.docker.com/compose/gettingstarted/

## Build the docker image from source
```sh
docker build . -t marcpartensky/website
```
Build usually last 5 minutes.

## Add me as a contact
![qrcode](./static/qrcode.svg)
**Scan to add me as a contact**

## Bonus

## Heroku Buildpacks

```
heroku/python
heroku/node
https://github.com/weibeld/heroku-buildpack-graphviz
```
