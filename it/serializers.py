from rest_framework import serializers
from .models import *

# ==================================================
# IT Order Serializers Section Start
# ==================================================
class IT_OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Order
        # fields = '__all__'
        exclude = ['user']
        read_only_fields = ('created_at', 'last_update_at')


class IT_Order_Work_DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Order_Work_Document
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


class IT_OrderAdminNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Order_Admin_Note
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


# ==================================================
# IT Order Serializers Section End
# ==================================================




# ==================================================
# IT Order Payment Serializers Section Start
# ==================================================
class ITPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Payment
        fields = '__all__'

class ITBankPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_BankPayment
        fields = '__all__'

class ITMobilePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_MobilePayment
        fields = '__all__'

class ITOfflinePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_OfflinePayment
        fields = '__all__'

# ==================================================
# IT Order Payment Serializers Section End
# ==================================================


# ==================================================
# IT Order Refund Serializers Section Start
# ==================================================
class ITRefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Refund
        fields = '__all__'

class ITBankRefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Bank_Refund
        fields = '__all__'

class ITMobileRefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Mobile_Refund
        fields = '__all__'
# ==================================================
# IT Order Refund Serializers Section End
# ==================================================




# ==================================================
# IT Payment Method Serializers For Whole Website Start
# ==================================================
class ITBankSerializerit(serializers.ModelSerializer):
    class Meta:
        model = IT_Bank
        fields = '__all__'

class ITMobileWalletSerializerit(serializers.ModelSerializer):
    class Meta:
        model = IT_MobileWallet
        fields = '__all__'

class ITOfflineCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_OfflineCheck
        fields = '__all__'

# ==================================================
# IT Payment Method Serializers For Whole Website End
# ==================================================


