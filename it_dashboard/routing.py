from django.urls import path
from . import consumers

# Define your WebSocket URL patterns
websocket_urlpatterns = [
    path(r'ws/it/', consumers.Consumer.as_asgi()),
]
