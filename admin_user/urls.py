from django.urls import path, include
from .views import *

urlpatterns = [
    path('', api_root, name='api-root'),
    
    # User List And Create Api Url====================================
    path('user-list/', AdminUserCreationAPI.as_view(), name='user-list'),
    path('user-list/<int:pk>/', AdminUserUpdateDeleteAPI.as_view(), name='user'),
    
    # User Login Api Url====================================
    path('login/', AdminLogin.as_view(), name='api-admin-login'),
    path('login/<token>/', AdminLogin.as_view(), name='api-login-token'),
    path('login-verification/', AdminLoginOTPVerification.as_view(), name='admin-login-otp-verification'),
    
    # User Forget & Reset Password Api Url====================================
    path('forget-password/', AdminForgetPasswordAPIView.as_view(), name='api-admin-forget-password'),
    path('reset-password/', AdminResetPasswordAPIView.as_view(), name='api-admin-reset-password'),
    
    # User Change Password Api Url====================================
    path('change-password/', AdminChangePasswordAPIView.as_view(), name='admin-change-password-api'),
    
    # Delete requests
    path('delete-requests/', ListDeleteRequestUsers.as_view(), name='list-delete-request-users'),
    
    # approve delete requests
    path('approve-profile-delete-request/<int:pk>', ApproveUserProfileDeleteRequestAPIView.as_view(), name='approve-profile-delete-request'),
]
