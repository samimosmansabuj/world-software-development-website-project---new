from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *




# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('test_socket', test_socket, name='test_socket'),
]
