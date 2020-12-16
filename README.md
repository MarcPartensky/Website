# Website

This is the code for my personal website.
[https://websiteofmarcpartensky.herokuapp.com/](https://websiteofmarcpartensky.herokuapp.com/)

## Light theme
[![light theme](https://cdn.discordapp.com/attachments/702863598761803806/782335262499930112/light.png)](https://websiteofmarcpartensky.herokuapp.com)

## Dark theme
[![dark theme](https://cdn.discordapp.com/attachments/702863598761803806/782334455385555014/dark.png)](https://websiteofmarcpartensky.herokuapp.com?theme=dark)

## Install

### Docker (still failing)
```sh
docker push marcpartensky/website
```

### From source
```sh
git clone https://github.com/marcpartensky/website
pip install -r requirements.txt
gunicorn django_project.wsgi
```

## QR Code
![qrcode](./static/qrcode.svg)
**Scan to add me as a contact**
