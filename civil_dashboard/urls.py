from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .sound_views import *

router = DefaultRouter()
router.register(r'website-logo', Civil_WebsiteLogoViewSet, basename='civil-website-logo')
router.register(r'website-banner', Civil_WebsiteBannerViewSet, basename='civil-website-banner')
router.register(r'two-card-customer-feedback', CivilTwoCardCustomerFeedbackViewSet, basename='civil-two-card-customer-feedback')
router.register(r'three-card-section', CivilThreeCardSectionViewSet, basename='civil-three-card-section')
router.register(r'four-card-section', CivilFourCardSectionViewSet, basename='civil-four-card-section')
router.register(r'card-template', Civil_CardTemplateViewSet, basename='civil-card-template')
router.register(r'blog-card', Civil_BlogCardViewSet, basename='civil-blog-card')

router.register(r'arcitecture-images', Civil_Arcitecture_ImagesViewSet, basename='civil-arcitecture-images')
router.register(r'arcitecture', Civil_ArcitectureViewSet, basename='civil-arcitecture')
router.register(r'feature-work-category', Civil_Feature_Work_CategoryViewSet, basename='civil-feature-work-category')
router.register(r'feature-work', Civil_Feature_WorkViewSet, basename='civil-feature-work')

router.register(r'our-services', Civil_Our_ServicesViewSet, basename='civil-our-services')
router.register(r'notice-board', Civil_Notice_BoardViewSet, basename='civil-notice-board')
router.register(r'order-card', Civil_Order_CardViewSet, basename='civil-order-card')
router.register(r'security-page', Civil_Security_PageViewSet, basename='civil-security-page')
router.register(r'company-member', Civil_Company_MemberViewSet, basename='civil-company-member')

router.register(r'time-data', Civil_TimeDataViewSet, basename='civil-time-data')
router.register(r'homepage-segment', Civil_Homepage_SegmentViewSet, basename='civil-homepage-segment')
router.register(r'support-company-logo', Civil_Support_Company_LogoViewSet, basename='civil-support-company-logo')
router.register(r'global-location', Civil_Global_LocationViewSet, basename='civil-global-location')
router.register(r'contact-us', Civil_Contact_UsViewSet, basename='civil-contact-us')

router.register(r'office-address', Civil_Office_AddressViewSet, basename='civil-office-address')
router.register(r'payment-logo', Civil_Payment_LogoViewSet, basename='civil-payment-logo')
router.register(r'social-media', Civil_Social_MediaViewSet, basename='civil-social-media')
router.register(r'subscriptions', Civil_SubscriptionsViewSet, basename='civil-subscriptions')
router.register(r'footer-section-topics', CivilFooterSectionTopicsViewSet, basename='civil-footer-section-topics')
router.register(r'footer-section-1', CivilFooterSection1ViewSet, basename='civil-footer-section-1')
router.register(r'footer-section-2', CivilFooterSection2ViewSet, basename='civil-footer-section-2')
router.register(r'footer-section-3', CivilFooterSection3ViewSet, basename='civil-footer-section-3')


# ==================================================
# Sound Urls Router For Whole Website Start
# ==================================================
sound_router = DefaultRouter()
sound_router.register(r'live-chat-admin-sound', CivilLiveChatAdminSoundAPI, basename='civil-live-chat-admin-sound')
sound_router.register(r'user-sound', CivilUserSoundAPI, basename='civil-user-sound')
sound_router.register(r'user-order-sound', CivilUserOrderSoundAPI, basename='civil-user-order-sound')
# ==================================================
# Sound Urls Router For Whole Website End
# ==================================================

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/home/', include(router.urls)),
    path('api/sound/', include(sound_router.urls)),

    path('test_socket', test_socket, name='test_socket'),
]
