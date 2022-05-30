# editor/routing.py
from django.urls import re_path

# from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/code/(?P<room_name>\w+)/$", consumers.EditorConsumer.as_asgi()),
    # url(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
