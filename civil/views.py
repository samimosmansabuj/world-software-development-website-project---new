from .models import *
from .serializers import *
from rest_framework import viewsets
from django_filters import rest_framework
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser



# ==================================================
# Civil Order Views Section Start
# ==================================================
class Civil_OrderAPI(viewsets.ModelViewSet):
    queryset = Civil_Order.objects.all()
    serializer_class = Civil_OrderSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class Civil_Order_Work_DocumentAPI(viewsets.ModelViewSet):
    queryset = Civil_Order_Work_Document.objects.all()
    serializer_class = Civil_Order_Work_DocumentSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

class Civil_OrderAdminNoteAPI(viewsets.ModelViewSet):
    queryset = Civil_Order_Admin_Note.objects.all()
    serializer_class = Civil_OrderAdminNoteSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

# ==================================================
# Civil Order Views Section End
# ==================================================




# ==================================================
# Civil Order Payment Views Section Start
# ==================================================
class CivilPaymentFilter(rest_framework.FilterSet):
    class Meta:
        model = Civil_Payment
        fields = ['payment_type', 'payment_method']

class CivilPaymentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Civil_Payment.objects.all()
    serializer_class = CivilPaymentSerializer
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_class = CivilPaymentFilter


class CivilBankPaymentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Civil_BankPayment.objects.all()
    serializer_class = CivilBankPaymentSerializer
    parser_classes = [MultiPartParser]

class CivilMobilePaymentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Civil_MobilePayment.objects.all()
    serializer_class = CivilMobilePaymentSerializer
    parser_classes = [MultiPartParser]

class CivilOfflinePaymentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Civil_OfflinePayment.objects.all()
    serializer_class = CivilOfflinePaymentSerializer
    parser_classes = [MultiPartParser]

# ==================================================
# Civil Order Payment Views Section End
# ==================================================



# ==================================================
# Civil Order Refund Views Section Start
# ==================================================
class CivilRefundFilter(rest_framework.FilterSet):
    class Meta:
        model = Civil_Refund
        fields = ['refund_method']       

class CivilRefundViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Civil_Refund.objects.all()
    serializer_class = CivilRefundSerializer
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_class = CivilRefundFilter
    parser_classes = [MultiPartParser]

class CivilBankRefundViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Civil_Bank_Refund.objects.all()
    serializer_class = CivilBankRefundSerializer

class CivilMobileRefundViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Civil_Mobile_Refund.objects.all()
    serializer_class = CivilMobileRefundSerializer
# ==================================================
# Civil Order Refund Views Section End
# ==================================================




# ==================================================
# Payment Method Views For Whole Website Start
# ==================================================
class CivilBankViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Civil_Bank.objects.all()
    serializer_class = CivilBankSerializerit
    parser_classes = [MultiPartParser]

class CivilMobileWalletViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Civil_MobileWallet.objects.all()
    serializer_class = CivilMobileWalletSerializerit
    parser_classes = [MultiPartParser]

class CivilOfflineCheckViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Civil_OfflineCheck.objects.all()
    serializer_class = CivilOfflineCheckSerializer

# ==================================================
# Payment Method Views For Whole Website End
# ==================================================


