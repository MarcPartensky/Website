#!/usr/bin/env python

"""
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

# from dotenv import load_dotenv
# load_dotenv()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
# print('DJANGO_SETTINGS_MODULE:', os.environ.get('DJANGO_SETTINGS_MODULE'))

import django

django.setup()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from . import routing


# print(routing.websocket_urlpatterns)

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns)),
    }
)
