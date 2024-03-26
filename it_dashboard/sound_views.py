from django.shortcuts import render
from .models import *
from .sound_serializers import *
from rest_framework import viewsets





# ==================================================
# Website Sound System Views For Whole Website Start
# ==================================================

# Live_Chat_Admin Model API Views==================================
class ITLiveChatAdminSoundAPI(viewsets.ModelViewSet):
    queryset = IT_Live_Chat_Admin_Sound.objects.all()
    serializer_class = IT_LiveChatAdminSoundSerializer

# User_Sound Model API Views==================================
class ITUserSoundAPI(viewsets.ModelViewSet):
    queryset = IT_User_Sound.objects.all()
    serializer_class = IT_UserSoundSerializer

# User_Order_Sound Model API Views==================================
class ITUserOrderSoundAPI(viewsets.ModelViewSet):
    queryset = IT_User_Order_Sound.objects.all()
    serializer_class = IT_UserOrderSoundSerializer

# ==================================================
# Website Sound System Views For Whole Website End
# ==================================================

