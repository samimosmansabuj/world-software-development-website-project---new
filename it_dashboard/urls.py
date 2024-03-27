from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .sound_views import *

# Create a router and register the viewsets with it.
router = DefaultRouter()
# router.register(r'website-logo', IT_WebsiteLogoViewSet, basename='it-website-logo')
# router.register(r'website-banner', IT_WebsiteBannerViewSet, basename='it-website-banner')
# router.register(r'two-card-customer-feedback', ITTwoCardCustomerFeedbackViewSet, basename='it-two-card-customer-feedback')
# router.register(r'three-card-section', ITThreeCardSectionViewSet, basename='it-three-card-section')
# router.register(r'four-card-section', ITFourCardSectionViewSet, basename='it-four-card-section')
# router.register(r'card-template', IT_CardTemplateViewSet, basename='it-card-template')
# router.register(r'blog-card', IT_BlogCardViewSet, basename='it-blog-card')

# router.register(r'technology-icon', IT_Technology_IconViewSet, basename='it-technology-icon')
# router.register(r'technology', IT_TechnologyViewSet, basename='it-technology')
# router.register(r'our-services', IT_Our_ServicesViewSet, basename='it-our-services')
# router.register(r'notice-board', IT_Notice_BoardViewSet, basename='it-notice-board')
# router.register(r'order-card', IT_Order_CardViewSet, basename='it-order-card')
# router.register(r'security-page', IT_Security_PageViewSet, basename='it-security-page')
# router.register(r'company-member', IT_Company_MemberViewSet, basename='it-company-member')

# router.register(r'time-data', IT_TimeDataViewSet, basename='it-time-data')
# router.register(r'homepage-segment', IT_Homepage_SegmentViewSet, basename='it-homepage-segment')
# router.register(r'support-company-logo', IT_Support_Company_LogoViewSet, basename='it-support-company-logo')
# router.register(r'global-location', IT_Global_LocationViewSet, basename='it-global-location')
# router.register(r'contact-us', IT_Contact_UsViewSet, basename='it-contact-us')

# router.register(r'office-address', IT_Office_AddressViewSet, basename='it-office-address')
# router.register(r'payment-logo', IT_Payment_LogoViewSet, basename='it-payment-logo')
# router.register(r'social-media', IT_Social_MediaViewSet, basename='it-social-media')
# router.register(r'subscriptions', IT_SubscriptionsViewSet, basename='it-subscriptions')
# router.register(r'footer-section-topics', ITFooterSectionTopicsViewSet, basename='it-footer-section-topics')
# router.register(r'footer-section-1', ITFooterSection1ViewSet, basename='it-footer-section-1')
# router.register(r'footer-section-2', ITFooterSection2ViewSet, basename='it-footer-section-2')
# router.register(r'footer-section-3', ITFooterSection3ViewSet, basename='it-footer-section-3')



# ==================================================
# Sound Urls Router For Whole Website Start
# ==================================================
sound_router = DefaultRouter()
sound_router.register(r'live-chat-admin-sound', ITLiveChatAdminSoundAPI, basename='it-live-chat-admin-sound')
sound_router.register(r'user-sound', ITUserSoundAPI, basename='it-user-sound')
sound_router.register(r'user-order-sound', ITUserOrderSoundAPI, basename='it-user-order-sound')
# ==================================================
# Sound Urls Router For Whole Website End
# ==================================================




# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/home/', include(router.urls)),
    path('api/sound/', include(sound_router.urls)),
]
