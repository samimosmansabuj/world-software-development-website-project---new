from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .sound_views import *

router = DefaultRouter()
router.register(r'logo', LogoViewSet, basename='logo')
router.register(r'banners', BannerViewSet)
router.register(r'two-card-customer-feedback', TwoCardCustomerFeedbackViewSet)
router.register(r'three-card-sections', ThreeCardSectionViewSet)
router.register(r'four-card-sections', FourCardSectionViewSet)
router.register(r'card-templates', CardTemplateViewSet)
router.register(r'blog-cards', BlogCardViewSet)
router.register(r'time-data', TimeDataViewSet)
router.register(r'homepage-segments', HomepageSegmentViewSet)
router.register(r'support-company-logos', SupportCompanyLogoViewSet)
router.register(r'global-locations', GlobalLocationViewSet)
router.register(r'contact-us', ContactUsViewSet)
router.register(r'technology-icons', TechnologyIconViewSet)
router.register(r'technologies', TechnologyViewSet)
router.register(r'civil-arcitecture-images', Civil_Arcitecture_ImagesViewSet)
router.register(r'civil-arcitectures', Civil_ArcitectureViewSet)
router.register(r'civil-feature-work-categories', Civil_Feature_Work_CategoryViewSet)
router.register(r'civil-feature-works', Civil_Feature_WorkViewSet)
router.register(r'our-services', OurServicesViewSet)
router.register(r'notice-boards', NoticeBoardViewSet)
router.register(r'order-cards', OrderCardViewSet)
router.register(r'security-pages', SecurityPageViewSet)
router.register(r'company-members', CompanyMemberViewSet)
router.register(r'office-addresses', OfficeAddressViewSet)
router.register(r'payment-logos', PaymentLogoViewSet)
router.register(r'social-medias', SocialMediaViewSet)
router.register(r'subscriptions', SubscriptionsViewSet)
router.register(r'footer-section-topics', FooterSectionTopicsViewSet)
router.register(r'footer-section-1', FooterSection1ViewSet)
router.register(r'footer-section-2', FooterSection2ViewSet)
router.register(r'footer-section-3', FooterSection3ViewSet)


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


urlpatterns = [
    path('', include(router.urls)),
    path('sound/', include(sound_router.urls)),
    
    path('order/application/', OrderApplicationViews.as_view(), name='order_application')
]

