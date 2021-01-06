import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from . import routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")

# print(routing.websocket_urlpatterns)

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
      URLRouter(routing.websocket_urlpatterns)
    ),
})
