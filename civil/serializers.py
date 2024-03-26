from rest_framework import serializers
from .models import *

# ==================================================
# Civil Order Serializers Section Start
# ==================================================
class Civil_OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Order
        exclude = ['user']
        read_only_fields = ('created_at', 'last_update_at')

class Civil_Order_Work_DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Order_Work_Document
        fields = '__all__'

class Civil_OrderAdminNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Order_Admin_Note
        fields = '__all__'

# ==================================================
# Civil Order Serializers Section End
# ==================================================




# ==================================================
# Civil Order Payment Section Start
# ==================================================

class CivilPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Payment
        fields = '__all__'

class CivilBankPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_BankPayment
        fields = '__all__'

class CivilMobilePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_MobilePayment
        fields = '__all__'

class CivilOfflinePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_OfflinePayment
        fields = '__all__'

# ==================================================
# Civil Order Payment Section End
# ==================================================



# ==================================================
# Civil Order Refund serializers Section Start
# ==================================================
class CivilRefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Refund
        fields = '__all__'

class CivilBankRefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Bank_Refund
        fields = '__all__'

class CivilMobileRefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Mobile_Refund
        fields = '__all__'
# ==================================================
# Civil Order Refund serializers Section End
# ==================================================



# ==================================================
# Payment Method Serializers For Whole Website Start
# ==================================================
class CivilBankSerializerit(serializers.ModelSerializer):
    class Meta:
        model = Civil_Bank
        fields = '__all__'

class CivilMobileWalletSerializerit(serializers.ModelSerializer):
    class Meta:
        model = Civil_MobileWallet
        fields = '__all__'

class CivilOfflineCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_OfflineCheck
        fields = '__all__'

# ==================================================
# Payment Method Serializers For Whole Website End
# ==================================================



