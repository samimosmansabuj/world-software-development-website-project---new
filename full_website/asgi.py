"""
ASGI config for full_website project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""


# import os
# from django.core.asgi import get_asgi_application
# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.urls import path
# from civil_dashboard.routing import websocket_urlpatterns as civil_websocket_urlpatterns

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'full_website.settings')

# # Combine websocket patterns from different apps directly
# django_asgi_app = get_asgi_application()

# websocket_urlpatterns = [
#     path('civil_dashboard/', URLRouter(civil_websocket_urlpatterns)),
#     # Assuming admin_user_websocket_urlpatterns follows a similar pattern, you'd include it like so:
#     # path('admin_user/', URLRouter(admin_user_websocket_urlpatterns)),
# ]

# application = ProtocolTypeRouter({
#     "http": django_asgi_app,
#     "websocket": AuthMiddlewareStack(
#         URLRouter(websocket_urlpatterns)
#     ),
# })

from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import os

# Import websocket_urlpatterns from each app
from civil_dashboard.routing import websocket_urlpatterns as civil_websocket_urlpatterns
from it_dashboard.routing import websocket_urlpatterns as it_websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'full_website.settings')

# Combine websocket_urlpatterns from all apps
combined_websocket_urlpatterns = civil_websocket_urlpatterns + it_websocket_urlpatterns

application = ProtocolTypeRouter({
    "http": get_asgi_application(), 
    "websocket": AuthMiddlewareStack(
        URLRouter(
            combined_websocket_urlpatterns 
        )
    ),
})



# import os
# from django.core.asgi import get_asgi_application
# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from full_website.routing import websocket_urlpatterns

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'full_website.settings')

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),  # Handle HTTP requests
#     "websocket": AuthMiddlewareStack(  # Handle WebSocket requests
#         URLRouter(
#             websocket_urlpatterns  # Use the centralized WebSocket URL patterns
#         )
#     ),
# })
