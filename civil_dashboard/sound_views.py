from django.shortcuts import render
from .models import *
from .sound_serializers import *
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated




# ==================================================
# Website Sound System Views For Whole Website Start
# ==================================================

# Live_Chat_Admin Model API Views==================================
class CivilLiveChatAdminSoundAPI(viewsets.ModelViewSet):
    queryset = Civil_Live_Chat_Admin_Sound.objects.all()
    serializer_class = Civil_LiveChatAdminSoundSerializer

# User_Sound Model API Views==================================
class CivilUserSoundAPI(viewsets.ModelViewSet):
    queryset = Civil_User_Sound.objects.all()
    serializer_class = Civil_UserSoundSerializer

# User_Order_Sound Model API Views==================================
class CivilUserOrderSoundAPI(viewsets.ModelViewSet):
    queryset = Civil_User_Order_Sound.objects.all()
    serializer_class = Civil_UserOrderSoundSerializer

# ==================================================
# Website Sound System Views For Whole Website End
# ==================================================

