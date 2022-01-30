[![Docker](https://github.com/MarcPartensky/Website/actions/workflows/docker-push.yml/badge.svg)](https://github.com/MarcPartensky/Website/actions/workflows/docker-push.yml)
[![CodeQL](https://github.com/MarcPartensky/Website/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/MarcPartensky/Website/actions/workflows/codeql-analysis.yml)

# Website

This is the code of my personal website.
[https://marcpartensky.com/](https://marcpartensky.com/)

[![website](https://cdn.discordapp.com/attachments/507519157387132940/937471879776710676/website.png)](https://marcpartensky.com)


## Light theme
[![light theme](https://cdn.discordapp.com/attachments/507519157387132940/937472721015668766/website1.png)](https://marcpartensky.com)

## Dark theme
[![dark theme](https://cdn.discordapp.com/attachments/507519157387132940/937472943422849044/website2.png)](https://marcpartensky.com?theme=dark)

## Install

### From [source](https://github.com/MarcPartensky/Website) (requires [git](https://git-scm.com/), [python](https://www.python.org/), [pip](https://pip.pypa.io/en/stable/installing/))
```sh
git clone https://github.com/marcpartensky/website

pip install -r requirements.txt
# or with pipenv (recommended, install pipenv with pip install pipenv)
pipenv install

./manage.py runserver
```

## Deploy with [Docker](docker.com)

### Run website as standalone 

#### run unsecured for quick test
```sh
docker run -it \
	-e SECRET_KEY=$(openssl rand -base64 32) \
	-p 8080:80 \
	marcpartensky/website
```

#### or run with ssl certificate
```sh
docker run -it \
	-env CERT \ # You must export a ssl certificate path
	-env KEY \ # You must export a pem key path
	-e SECRET_KEY=$(openssl rand -base64 32) \
	-p 8443:443 \
	marcpartensky/website
```

### Or run with middleware (databases)
```sh
git clone https://github.com/marcpartensky/website
cd website
docker-compose up
```

## Build the docker image from source
```sh
docker build . -t marcpartensky/website
```
Build usually last 5 minutes.

## Add me as a contact
![qrcode](./static/qrcode.svg)
**Scan to add me as a contact**

# Bonus

## Notes
author: Marc Partensky
created: 8/10/2019

## Heroku Buildpacks

```
heroku/python
heroku/node
https://github.com/weibeld/heroku-buildpack-graphviz
```
