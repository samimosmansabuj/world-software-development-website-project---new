from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *



router = DefaultRouter()
router.register(r'social-link', SocialLinkAPI)

urlpatterns = [
    path('', include(router.urls)),
    
    # User Profile Api Url====================================
    path('user-profile/', UserProfileView.as_view(), name='user_profile'),
    path('profile/', UserProfileAPI.as_view(), name='user-profile'),
    path('company-information/', CompanyInformatinoAPI.as_view(), name='company-information'),
    path('address/', AddressAPI.as_view(), name='address'),
    
    # User Forget & Reset Password - Change Password Api Url====================================
    path('change-password/', ChangePasswordAPIView.as_view(), name='change-password-api'),
    path('forget-password/', ForgetPasswordAPIView.as_view(), name='api-forget-password'),
    path('reset-password/', ResetPasswordAPIView.as_view(), name='api-reset-password'),
    
    # User Authentication Credentials Api Url====================================
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('login/', LoginAPIView.as_view(), name='custom_token_obtain_pair'),
    path('register/', UserRegistrationAPIView.as_view(), name='user_registration'),
    path('verify-otp/', verify_otp, name='verify-otp'),
    path('regenerate-otp/', regenerate_otp, name='regenerate_otp'),
    
    # User Deleta Process Api Url====================================
    path('delete-profile-request/', DeleteProfileRequestAPIView.as_view(), name='delete-profile-request'),
    path('cancel-delete-profile-request/', CancelDeleteProfileRequestAPIView.as_view(), name='cancel-delete-profile-request'),
    
]

