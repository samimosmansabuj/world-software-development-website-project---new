import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'full_website.settings')

django.setup()

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from civil_dashboard.routing import websocket_urlpatterns as civil_websocket_urlpatterns
from it_dashboard.routing import websocket_urlpatterns as it_websocket_urlpatterns

combined_websocket_urlpatterns = civil_websocket_urlpatterns + it_websocket_urlpatterns

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            combined_websocket_urlpatterns
        )
    ),
})
