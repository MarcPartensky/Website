# chat/routing.py
from django.urls import re_path
# from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    path('ws/test/', consumers.TestConsummer.as_asgi()),
]
