from django.urls import path
from channels.routing import URLRouter
from . import consumers

# Define your WebSocket URL patterns
websocket_urlpatterns = [
    path(r'ws/civil/', consumers.Consumer.as_asgi()),
]
