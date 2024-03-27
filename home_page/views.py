from rest_framework import viewsets, filters
from django.db.models import Q
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from .models import *
from .serializers import *


class LogoViewSet(viewsets.ModelViewSet):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['section']

class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['section']

class TwoCardCustomerFeedbackViewSet(viewsets.ModelViewSet):
    queryset = TwoCardCustomerFeedback.objects.all()
    serializer_class = TwoCardCustomerFeedbackSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['section']

class ThreeCardSectionViewSet(viewsets.ModelViewSet):
    queryset = ThreeCardSection.objects.all()
    serializer_class = ThreeCardSectionSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['section']

class FourCardSectionViewSet(viewsets.ModelViewSet):
    queryset = FourCardSection.objects.all()
    serializer_class = FourCardSectionSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['section']


class CardTemplateFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    tag = django_filters.CharFilter(field_name='tag', lookup_expr='icontains')
    url = django_filters.CharFilter(field_name='url', lookup_expr='icontains')
    price = django_filters.NumberFilter(field_name='price', lookup_expr='icontains')
    class Meta:
        model = CardTemplate
        fields = ['section']

class CardTemplateViewSet(viewsets.ModelViewSet):
    queryset = CardTemplate.objects.all()
    serializer_class = CardTemplateSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = CardTemplateFilter
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(tag__icontains=search_query) |
                Q(url__icontains=search_query)
            )
        return queryset


class BlogCardFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    tag = django_filters.CharFilter(field_name='tag', lookup_expr='icontains')
    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')
    class Meta:
        model = BlogCard
        fields = ['section']

class BlogCardViewSet(viewsets.ModelViewSet):
    queryset = BlogCard.objects.all()
    serializer_class = BlogCardSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = BlogCardFilter
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(tag__icontains=search_query) |
                Q(description__icontains=search_query)
            )
        return queryset


class TimeDataViewSet(viewsets.ModelViewSet):
    queryset = TimeData.objects.all()
    serializer_class = TimeDataSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]

class HomepageSegmentViewSet(viewsets.ModelViewSet):
    queryset = HomepageSegment.objects.all()
    serializer_class = HomepageSegmentSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['section']

class SupportCompanyLogoViewSet(viewsets.ModelViewSet):
    queryset = SupportCompanyLogo.objects.all()
    serializer_class = SupportCompanyLogoSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['section']


class GlobalLocationFilter(django_filters.FilterSet):
    country_name = django_filters.CharFilter(field_name='country_name', lookup_expr='icontains')
    office_address = django_filters.CharFilter(field_name='office_address', lookup_expr='icontains')
    contact_details = django_filters.CharFilter(field_name='contact_details', lookup_expr='icontains')
    class Meta:
        model = GlobalLocation
        fields = ['section']

class GlobalLocationViewSet(viewsets.ModelViewSet):
    queryset = GlobalLocation.objects.all()
    serializer_class = GlobalLocationSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = GlobalLocationFilter
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(country_name__icontains=search_query) |
                Q(office_address__icontains=search_query) |
                Q(contact_details__icontains=search_query)
            )
        return queryset



class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['section']


# ===========================Only For IT Start=================================
class TechnologyIconViewSet(viewsets.ModelViewSet):
    queryset = TechnologyIcon.objects.all()
    serializer_class = TechnologyIconSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]

class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]
# ===========================Only For IT End=================================

# ===========================Only For Civil Start=================================
class Civil_Arcitecture_ImagesViewSet(viewsets.ModelViewSet):
    queryset = Civil_Arcitecture_Images.objects.all()
    serializer_class = Civil_Arcitecture_ImagesSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]


class Civil_ArcitectureFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    plan_details = django_filters.CharFilter(field_name='plan_details', lookup_expr='icontains')
    describtion = django_filters.CharFilter(field_name='describtion', lookup_expr='icontains')
    class Meta:
        model = Civil_Arcitecture
        fields = []

class Civil_ArcitectureViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_Arcitecture.objects.all()
    serializer_class = Civil_ArcitectureSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = Civil_ArcitectureFilter
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(plan_details__icontains=search_query) |
                Q(describtion__icontains=search_query)
            )
        return queryset


class Civil_Feature_Work_CategoryViewSet(viewsets.ModelViewSet):
    queryset = Civil_Feature_Work_Category.objects.all()
    serializer_class = Civil_Feature_Work_CategorySerializer
    permission_classes = [AllowAny]

class Civil_Feature_WorkViewSet(viewsets.ModelViewSet):
    queryset = Civil_Feature_Work.objects.all()
    serializer_class = Civil_Feature_WorkSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]
# ===========================Only For Civil End=================================


class OurServicesFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    tags = django_filters.CharFilter(field_name='tags', lookup_expr='icontains')
    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')
    class Meta:
        model = OurServices
        fields = ['section']

class OurServicesViewSet(viewsets.ModelViewSet):
    queryset = OurServices.objects.all()
    serializer_class = OurServicesSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = OurServicesFilter
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(tags__icontains=search_query) |
                Q(description__icontains=search_query)
            )
        return queryset


class NoticeBoardFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    date = django_filters.DateFilter(field_name='date', lookup_expr='icontains')
    class Meta:
        model = NoticeBoard
        fields = ['section','status']

class NoticeBoardViewSet(viewsets.ModelViewSet):
    queryset = NoticeBoard.objects.all()
    serializer_class = NoticeBoardSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = NoticeBoardFilter
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query)
            )
        return queryset


class OrderCard_Filter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    class Meta:
        model = OrderCard
        fields = ['section']

class OrderCardViewSet(viewsets.ModelViewSet):
    queryset = OrderCard.objects.all()
    serializer_class = OrderCardSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = OrderCard_Filter
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query)
            )
        return queryset


class SecurityPageViewSet(viewsets.ModelViewSet):
    queryset = SecurityPage.objects.all()
    serializer_class = SecurityPageSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['section']



class CompanyMemberFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    email = django_filters.CharFilter(field_name='email', lookup_expr='icontains')
    phone_number = django_filters.CharFilter(field_name='phone_number', lookup_expr='icontains')
    address = django_filters.CharFilter(field_name='address', lookup_expr='icontains')
    class Meta:
        model = CompanyMember
        fields = ['section']

class CompanyMemberViewSet(viewsets.ModelViewSet):
    queryset = CompanyMember.objects.all()
    serializer_class = CompanyMemberSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = CompanyMemberFilter
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(name__icontains=search_query) |
                Q(email__icontains=search_query) |
                Q(phone_number__icontains=search_query) |
                Q(address__icontains=search_query)
            )
        return queryset



class OfficeAddressViewSet(viewsets.ModelViewSet):
    queryset = OfficeAddress.objects.all()
    serializer_class = OfficeAddressSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['section']

class PaymentLogoViewSet(viewsets.ModelViewSet):
    queryset = PaymentLogo.objects.all()
    serializer_class = PaymentLogoSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['section']

class SocialMediaViewSet(viewsets.ModelViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['section']

class SubscriptionsViewSet(viewsets.ModelViewSet):
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['section']

class FooterSectionTopicsViewSet(viewsets.ModelViewSet):
    queryset = FooterSectionTopics.objects.all()
    serializer_class = FooterSectionTopicsSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['section']

class FooterSection1ViewSet(viewsets.ModelViewSet):
    queryset = FooterSection1.objects.all()
    serializer_class = FooterSection1Serializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['section']

class FooterSection2ViewSet(viewsets.ModelViewSet):
    queryset = FooterSection2.objects.all()
    serializer_class = FooterSection2Serializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['section']

class FooterSection3ViewSet(viewsets.ModelViewSet):
    queryset = FooterSection3.objects.all()
    serializer_class = FooterSection3Serializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['section']


