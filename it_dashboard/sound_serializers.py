from rest_framework import serializers
from .sound_models import *




# ==================================================
# Website Sound System Serializers For Whole Website Start
# ==================================================
class IT_LiveChatAdminSoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Live_Chat_Admin_Sound
        fields = '__all__'

class IT_UserSoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_User_Sound
        fields = '__all__'

class IT_UserOrderSoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_User_Order_Sound
        fields = '__all__'
# ==================================================
# Website Sound System Serializers For Whole Website End
# ==================================================