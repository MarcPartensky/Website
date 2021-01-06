# mysite/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat

# application = ProtocolTypeRouter({
#     # (http->django views is added by default)
#     'websocket': AuthMiddlewareStack(
#         URLRouter(
#             chat.routing.websocket_urlpatterns
#         )
#     ),
# })


# # django_project/routing.py
# from django.urls import re_path
# # import chat.routing

websocket_urlpatterns = []
websocket_urlpatterns += chat.routing.websocket_urlpatterns

# re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
# path('ws/chat', include('chat.routing')),
# re_path(r'ws/chat', consumers.ChatConsumer.as_asgi()),

