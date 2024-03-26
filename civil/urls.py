from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


# ==================================================
# Civil Order urls Section Start
# ==================================================
order_router = DefaultRouter()
order_router.register(r'civil_orders', Civil_OrderAPI, basename='civil_order')
order_router.register(r'civil_order_work_documents', Civil_Order_Work_DocumentAPI, basename='civil_order_work_document')
order_router.register(r'civil_order_admin_notes', Civil_OrderAdminNoteAPI, basename='civil_order_admin_note')
# ==================================================
# Civil Order urls Section End
# ==================================================


# ==================================================
# Civil Order Payment urls Section Start
# ==================================================
payment_router = DefaultRouter()
payment_router.register(r'civil-payments', CivilPaymentViewSet)
payment_router.register(r'civil-bank-payments', CivilBankPaymentViewSet)
payment_router.register(r'civil-mobile-payments', CivilMobilePaymentViewSet)
payment_router.register(r'civil-offline-payments', CivilOfflinePaymentViewSet, basename='civil-offline-payments')
# ==================================================
# Civil Order Payment urls Section End
# ==================================================


# ==================================================
# Civil Order Refund urls Section Start
# ==================================================
refund_router = DefaultRouter()
refund_router.register(r'civil-refunds', CivilRefundViewSet)
refund_router.register(r'civil-bank-refunds', CivilBankRefundViewSet)
refund_router.register(r'civil-mobile-refunds', CivilMobileRefundViewSet)
# ==================================================
# Civil Order Refund urls Section End
# ==================================================


# ==================================================
# Payment Method Urls Router For Whole Website Start
# ==================================================
payment_method_router = DefaultRouter()
payment_method_router.register(r'civil-banks', CivilBankViewSet, basename='civil-bank')
payment_method_router.register(r'civil-mobile-wallets', CivilMobileWalletViewSet, basename='civil-mobile-wallet')
payment_method_router.register(r'civil-offline-checks', CivilOfflineCheckViewSet, basename='civil-offline-checks')
# ==================================================
# Payment Method Urls Router For Whole Website End
# ==================================================


urlpatterns = [
    path('order/', include(order_router.urls)),
    path('payment/', include(payment_router.urls)),
    path('refund/', include(refund_router.urls)),
    path('payment-method/', include(payment_method_router.urls)),
]


