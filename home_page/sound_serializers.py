from rest_framework import serializers
from .sound_models import *

# ==================================================
# Website Sound System Serializers For Whole Website Start
# ==================================================
class Civil_LiveChatAdminSoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Live_Chat_Admin_Sound
        fields = '__all__'

class Civil_UserSoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_User_Sound
        fields = '__all__'

class Civil_UserOrderSoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_User_Order_Sound
        fields = '__all__'
# ==================================================
# Website Sound System Serializers For Whole Website End
# ==================================================