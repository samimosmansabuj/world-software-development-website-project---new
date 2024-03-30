from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from django_filters import rest_framework
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from admin_user.models import Admin_User

# ==================================================
# IT Order Views Section Start
# ==================================================

class IT_OrderAPI(viewsets.ModelViewSet):
    serializer_class = IT_OrderSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]
    
    def get_queryset(self):
        user = self.request.user
        queryset = IT_Order.objects.filter(is_only_me=True)
        if user.is_authenticated and queryset:
            if user.user_type == 'Admin':
                queryset = IT_Order.objects.all()
            elif user.user_type == 'Sub-Admin':
                queryset = IT_Order.objects.none()
            else:
                queryset = IT_Order.objects.all()
        else:
            queryset = IT_Order.objects.all()

        return queryset
    
    
    # # def initial(self, request, *args, **kwargs):
    # #     request.data['user'] = request.user.id
    # #     super().initial(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class IT_Order_Work_DocumentAPI(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = IT_Order_Work_Document.objects.all()
    serializer_class = IT_Order_Work_DocumentSerializer
    parser_classes = [MultiPartParser]

class IT_OrderAdminNoteAPI(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = IT_Order_Admin_Note.objects.all()
    serializer_class = IT_OrderAdminNoteSerializer
    parser_classes = [MultiPartParser]

# ==================================================
# IT Order Views Section End
# ==================================================




# ==================================================
# IT Order Payment Views Section Start
# ==================================================
class ITPaymentFilter(rest_framework.FilterSet):
    class Meta:
        model = IT_Payment
        fields = ['payment_type', 'payment_method']

class ITPaymentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = IT_Payment.objects.all()
    serializer_class = ITPaymentSerializer
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_class = ITPaymentFilter

class ITBankPaymentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = IT_BankPayment.objects.all()
    serializer_class = ITBankPaymentSerializer
    parser_classes = [MultiPartParser]

class ITMobilePaymentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = IT_MobilePayment.objects.all()
    serializer_class = ITMobilePaymentSerializer
    parser_classes = [MultiPartParser]

class ITOfflinePaymentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = IT_OfflinePayment.objects.all()
    serializer_class = ITOfflinePaymentSerializer
    parser_classes = [MultiPartParser]

# ==================================================
# IT Order Payment Views Section End
# ==================================================



# ==================================================
# IT Order Refund Views Section Start
# ==================================================
class ITRefundFilter(rest_framework.FilterSet):
    class Meta:
        model = IT_Refund
        fields = ['refund_method']

class ITRefundViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = IT_Refund.objects.all()
    serializer_class = ITRefundSerializer
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_class = ITRefundFilter
    parser_classes = [MultiPartParser]


class ITBankRefundViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = IT_Bank_Refund.objects.all()
    serializer_class = ITBankRefundSerializer

class ITMobileRefundViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = IT_Mobile_Refund.objects.all()
    serializer_class = ITMobileRefundSerializer

# ==================================================
# IT Order Refund Views Section End
# ==================================================


# ==================================================
# IT Payment Method Views For Whole Website Start
# ==================================================
class ITBankViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = IT_Bank.objects.all()
    serializer_class = ITBankSerializerit
    parser_classes = [MultiPartParser]

class ITMobileWalletViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = IT_MobileWallet.objects.all()
    serializer_class = ITMobileWalletSerializerit
    parser_classes = [MultiPartParser]

class ITOfflineCheckViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = IT_OfflineCheck.objects.all()
    serializer_class = ITOfflineCheckSerializer
    parser_classes = [MultiPartParser]

# ==================================================
# IT Payment Method Views For Whole Website End
# ==================================================



