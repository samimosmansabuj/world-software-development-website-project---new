# from rest_framework import viewsets
# import django_filters
# from rest_framework import filters
# from django_filters.rest_framework import DjangoFilterBackend
# from .models import *
# from .serializers import *
# from rest_framework.permissions import *
# from django.db.models import Q
# from rest_framework.parsers import MultiPartParser

# # Viewsets for Website Logo Section
# class IT_WebsiteLogoViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = IT_WebsiteLogo.objects.all()
#     serializer_class = IT_WebsiteLogoSerializer
#     parser_classes = [MultiPartParser]

# # Viewsets for Website Banner Section
# class IT_WebsiteBannerViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = IT_WebsiteBanner.objects.all()
#     serializer_class = IT_WebsiteBannerSerializer
#     parser_classes = [MultiPartParser]

# # Viewsets for Website 2 Card Section
# class ITTwoCardCustomerFeedbackViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = IT_TwoCardCustomerFeedback.objects.all()
#     serializer_class = ITTwoCardCustomerFeedbackSerializer
#     parser_classes = [MultiPartParser]

# # Viewsets for Website 3 Card Section
# class ITThreeCardSectionViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = IT_ThreeCardSection.objects.all()
#     serializer_class = ITThreeCardSectionSerializer
#     parser_classes = [MultiPartParser]

# # Viewsets for Website 4 Card Section
# class ITFourCardSectionViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = IT_FourCardSection.objects.all()
#     serializer_class = ITFourCardSectionSerializer
#     parser_classes = [MultiPartParser]


# # ============Viewsets for Website Template Section Start============
# class IT_CardTemplateFilter(django_filters.FilterSet):
#     title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
#     tag = django_filters.CharFilter(field_name='tag', lookup_expr='icontains')
#     url = django_filters.CharFilter(field_name='url', lookup_expr='icontains')
#     price = django_filters.NumberFilter(field_name='price', lookup_expr='icontains')
#     class Meta:
#         model = IT_CardTemplate
#         fields = []

# class IT_CardTemplateViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = IT_CardTemplate.objects.all()
#     serializer_class = IT_CardTemplateSerializer
#     parser_classes = [MultiPartParser]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_class = IT_CardTemplateFilter
    
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         search_query = self.request.query_params.get('search', None)
#         if search_query:
#             queryset = queryset.filter(
#                 Q(title__icontains=search_query) |
#                 Q(tag__icontains=search_query) |
#                 Q(url__icontains=search_query)
#             )
#         return queryset
# # ============Viewsets for Website Template Section Start============


# # ============Viewsets for Website Blog Card Section Start============
# class IT_BlogCardFilter(django_filters.FilterSet):
#     title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
#     tag = django_filters.CharFilter(field_name='tag', lookup_expr='icontains')
#     description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')
#     class Meta:
#         model = IT_BlogCard
#         fields = []

# class IT_BlogCardViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = IT_BlogCard.objects.all()
#     serializer_class = IT_BlogCardSerializer
#     parser_classes = [MultiPartParser]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_class = IT_BlogCardFilter
    
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         search_query = self.request.query_params.get('search', None)
#         if search_query:
#             queryset = queryset.filter(
#                 Q(title__icontains=search_query) |
#                 Q(tag__icontains=search_query) |
#                 Q(description__icontains=search_query)
#             )
#         return queryset
# # ============Viewsets for Website Blog Card Section End============


# # Viewsets for Website Timedata Section
# class IT_TimeDataViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = IT_TimeData.objects.all()
#     serializer_class = IT_TimeDataSerializer

# # Viewsets for Website Segment Section
# class IT_Homepage_SegmentViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = IT_Homepage_Segment.objects.all()
#     serializer_class = IT_Homepage_SegmentSerializer

# # Viewsets for Website Company Logo Section
# class IT_Support_Company_LogoViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = IT_Support_Company_Logo.objects.all()
#     serializer_class = IT_Support_Company_LogoSerializer



# # ============Viewsets for Website Global Location Section End============
# class IT_Global_LocationFilter(django_filters.FilterSet):
#     country_name = django_filters.CharFilter(field_name='country_name', lookup_expr='icontains')
#     office_address = django_filters.CharFilter(field_name='office_address', lookup_expr='icontains')
#     contact_details = django_filters.CharFilter(field_name='contact_details', lookup_expr='icontains')
#     class Meta:
#         model = IT_Global_Location
#         fields = []

# class IT_Global_LocationViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = IT_Global_Location.objects.all()
#     serializer_class = IT_Global_LocationSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_class = IT_Global_LocationFilter
    
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         search_query = self.request.query_params.get('search', None)
#         if search_query:
#             queryset = queryset.filter(
#                 Q(country_name__icontains=search_query) |
#                 Q(office_address__icontains=search_query) |
#                 Q(contact_details__icontains=search_query)
#             )
#         return queryset
# # ============Viewsets for Website Global Location Section End============

# # Viewsets for Contact Section
# class IT_Contact_UsViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = IT_Contact_Us.objects.all()
#     serializer_class = IT_Contact_UsSerializer

# # Viewsets for Technology Section
# class IT_Technology_IconViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = IT_Technology_Icon.objects.all()
#     serializer_class = IT_Technology_IconSerializer
#     parser_classes = [MultiPartParser]

# class IT_TechnologyViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = IT_Technology.objects.all()
#     serializer_class = IT_TechnologySerializer
#     # parser_classes = [MultiPartParser]


# # Viewsets for Our Services Section
# class IT_Our_ServicesFilter(django_filters.FilterSet):
#     title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
#     tags = django_filters.CharFilter(field_name='tags', lookup_expr='icontains')
#     description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')
#     class Meta:
#         model = IT_Our_Services
#         fields = []

# class IT_Our_ServicesViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = IT_Our_Services.objects.all()
#     serializer_class = IT_Our_ServicesSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_class = IT_Our_ServicesFilter
    
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         search_query = self.request.query_params.get('search', None)
#         if search_query:
#             queryset = queryset.filter(
#                 Q(title__icontains=search_query) |
#                 Q(tags__icontains=search_query) |
#                 Q(description__icontains=search_query)
#             )
#         return queryset


# # Viewsets for Order Card Section
# class IT_Order_Card_Filter(django_filters.FilterSet):
#     title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
#     class Meta:
#         model = IT_Order_Card
#         fields = []

# class IT_Order_CardViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     permission_classes = (AllowAny,)
#     queryset = IT_Order_Card.objects.all()
#     serializer_class = IT_Order_CardSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_class = IT_Order_Card_Filter
    
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         search_query = self.request.query_params.get('search', None)
#         if search_query:
#             queryset = queryset.filter(
#                 Q(title__icontains=search_query)
#             )
#         return queryset
    

# # Viewsets for Security Page Section
# class IT_Security_PageViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = IT_Security_Page.objects.all()
#     serializer_class = IT_Security_PageSerializer



# # ============Viewsets for Website Notice Board Section Start============
# class IT_Notice_BoardFilter(django_filters.FilterSet):
#     title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
#     date = django_filters.DateFilter(field_name='date', lookup_expr='icontains')
#     status = django_filters.CharFilter(field_name='status', lookup_expr='icontains')
#     class Meta:
#         model = IT_Notice_Board
#         fields = []

# class IT_Notice_BoardViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = IT_Notice_Board.objects.all()
#     serializer_class = IT_Notice_BoardSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_class = IT_Notice_BoardFilter
    
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         search_query = self.request.query_params.get('search', None)
#         if search_query:
#             queryset = queryset.filter(
#                 Q(title__icontains=search_query)
#             )
#         return queryset
# # ============Viewsets for Website Notice Board Section End============

# # ============Viewsets for Website Company Member Section Start============
# class IT_CompanyMemberFilter(django_filters.FilterSet):
#     name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
#     title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
#     email = django_filters.CharFilter(field_name='email', lookup_expr='icontains')
#     phone_number = django_filters.CharFilter(field_name='phone_number', lookup_expr='icontains')
#     address = django_filters.CharFilter(field_name='address', lookup_expr='icontains')
#     class Meta:
#         model = IT_Company_Member
#         fields = []

# class IT_Company_MemberViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = IT_Company_Member.objects.all()
#     serializer_class = IT_Company_MemberSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_class = IT_CompanyMemberFilter
    
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         search_query = self.request.query_params.get('search', None)
#         if search_query:
#             queryset = queryset.filter(
#                 Q(title__icontains=search_query) |
#                 Q(name__icontains=search_query) |
#                 Q(email__icontains=search_query) |
#                 Q(phone_number__icontains=search_query) |
#                 Q(address__icontains=search_query)
#             )
#         return queryset
# # ============Viewsets for Website Company Member Section End============



# # ============Footer Section Viewsets Start============
# # Viewsets for Office Address Section
# class IT_Office_AddressViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = IT_Office_Address.objects.all()
#     serializer_class = IT_Office_AddressSerializer

# # Viewsets for Payment Logo Section
# class IT_Payment_LogoViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = IT_Payment_Logo.objects.all()
#     serializer_class = IT_Payment_LogoSerializer

# # Viewsets for Social Media Section
# class IT_Social_MediaViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = IT_Social_Media.objects.all()
#     serializer_class = IT_Social_MediaSerializer

# # Viewsets for Subscription Section
# class IT_SubscriptionsViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = IT_Subscriptions.objects.all()
#     serializer_class = IT_SubscriptionsSerializer

# # Viewsets for Footer Section
# class ITFooterSectionTopicsViewSet(viewsets.ModelViewSet):
#     queryset = IT_Footer_Section_Topics.objects.all()
#     serializer_class = ITFooterSectionTopicsSerializer

# class ITFooterSection1ViewSet(viewsets.ModelViewSet):
#     queryset = IT_Footer_Section_1.objects.all()
#     serializer_class = ITFooterSection1Serializer

# class ITFooterSection2ViewSet(viewsets.ModelViewSet):
#     queryset = IT_Footer_Section_2.objects.all()
#     serializer_class = ITFooterSection2Serializer

# class ITFooterSection3ViewSet(viewsets.ModelViewSet):
#     queryset = IT_Footer_Section_3.objects.all()
#     serializer_class = ITFooterSection3Serializer

# # ============Footer Section Viewsets End============

