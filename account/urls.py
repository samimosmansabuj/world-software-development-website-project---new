from django.urls import path
from .views import *

urlpatterns = [
    path('api/test/', TestView.as_view(), name='test_view'),
     
]
