# from rest_framework import viewsets
# import django_filters
# from rest_framework import filters
# from django_filters.rest_framework import DjangoFilterBackend
# from .models import *
# from .serializers import *
# from rest_framework.permissions import *
# from rest_framework.parsers import MultiPartParser
from django.shortcuts import render
# from django.db.models import Q

# # Viewsets for Website Logo Section
# class Civil_WebsiteLogoViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = Civil_WebsiteLogo.objects.all()
#     serializer_class = Civil_WebsiteLogoSerializer
#     parser_classes = [MultiPartParser]

# # Viewsets for Website Banner Section
# class Civil_WebsiteBannerViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = Civil_WebsiteBanner.objects.all()
#     serializer_class = Civil_WebsiteBannerSerializer
#     parser_classes = [MultiPartParser]




# # Viewsets for Website 2 Card Section
# class CivilTwoCardCustomerFeedbackViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = Civil_TwoCardCustomerFeedback.objects.all()
#     serializer_class = CivilTwoCardCustomerFeedbackSerializer
#     parser_classes = [MultiPartParser]

# # Viewsets for Website 3 Card Section
# class CivilThreeCardSectionViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = Civil_ThreeCardSection.objects.all()
#     serializer_class = CivilThreeCardSectionSerializer
#     parser_classes = [MultiPartParser]

# # Viewsets for Website 4 Card Section
# class CivilFourCardSectionViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = Civil_FourCardSection.objects.all()
#     serializer_class = CivilFourCardSectionSerializer
#     parser_classes = [MultiPartParser]



# # Viewsets for Website Template Card Section
# class Civil_CardTemplateFilter(django_filters.FilterSet):
#     title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
#     tag = django_filters.CharFilter(field_name='tag', lookup_expr='icontains')
#     url = django_filters.CharFilter(field_name='url', lookup_expr='icontains')
#     price = django_filters.NumberFilter(field_name='price', lookup_expr='icontains')
#     class Meta:
#         model = Civil_CardTemplate
#         fields = []

# class Civil_CardTemplateViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = Civil_CardTemplate.objects.all()
#     serializer_class = Civil_CardTemplateSerializer
#     parser_classes = [MultiPartParser]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_class = Civil_CardTemplateFilter
    
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




# # ============Viewsets for Website Blog Card Section Start============
# class Civil_BlogCardFilter(django_filters.FilterSet):
#     title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
#     tag = django_filters.CharFilter(field_name='tag', lookup_expr='icontains')
#     description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')
#     class Meta:
#         model = Civil_BlogCard
#         fields = []

# class Civil_BlogCardViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = Civil_BlogCard.objects.all()
#     serializer_class = Civil_BlogCardSerializer
#     parser_classes = [MultiPartParser]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_class = Civil_BlogCardFilter
    
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
# class Civil_TimeDataViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = Civil_TimeData.objects.all()
#     serializer_class = Civil_TimeDataSerializer

# # Viewsets for Website Segment Section
# class Civil_Homepage_SegmentViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = Civil_Homepage_Segment.objects.all()
#     serializer_class = Civil_Homepage_SegmentSerializer
#     parser_classes = [MultiPartParser]

# # Viewsets for Website Company Logo Section
# class Civil_Support_Company_LogoViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = Civil_Support_Company_Logo.objects.all()
#     serializer_class = Civil_Support_Company_LogoSerializer
#     parser_classes = [MultiPartParser]



# # ============Viewsets for Website Global Location Section End============
# class Civil_Global_LocationFilter(django_filters.FilterSet):
#     country_name = django_filters.CharFilter(field_name='country_name', lookup_expr='icontains')
#     office_address = django_filters.CharFilter(field_name='office_address', lookup_expr='icontains')
#     contact_details = django_filters.CharFilter(field_name='contact_details', lookup_expr='icontains')
#     class Meta:
#         model = Civil_Global_Location
#         fields = []

# class Civil_Global_LocationViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = Civil_Global_Location.objects.all()
#     serializer_class = Civil_Global_LocationSerializer
#     parser_classes = [MultiPartParser]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_class = Civil_Global_LocationFilter
    
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
# class Civil_Contact_UsViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = Civil_Contact_Us.objects.all()
#     serializer_class = Civil_Contact_UsSerializer



# # Viewsets for Architecture Section
# class Civil_Arcitecture_ImagesViewSet(viewsets.ModelViewSet):
#     queryset = Civil_Arcitecture_Images.objects.all()
#     serializer_class = Civil_Arcitecture_ImagesSerializer

# class Civil_ArcitectureFilter(django_filters.FilterSet):
#     title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
#     plan_details = django_filters.CharFilter(field_name='plan_details', lookup_expr='icontains')
#     describtion = django_filters.CharFilter(field_name='describtion', lookup_expr='icontains')
#     class Meta:
#         model = Civil_Arcitecture
#         fields = []

# class Civil_ArcitectureViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = Civil_Arcitecture.objects.all()
#     serializer_class = Civil_ArcitectureSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_class = Civil_ArcitectureFilter
    
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         search_query = self.request.query_params.get('search', None)
#         if search_query:
#             queryset = queryset.filter(
#                 Q(title__icontains=search_query) |
#                 Q(plan_details__icontains=search_query) |
#                 Q(describtion__icontains=search_query)
#             )
#         return queryset

# # Viewsets for Feature Work Section
# class Civil_Feature_WorkViewSet(viewsets.ModelViewSet):
#     queryset = Civil_Feature_Work.objects.all()
#     serializer_class = Civil_Feature_WorkSerializer

# class Civil_Feature_Work_CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Civil_Feature_Work_Category.objects.all()
#     serializer_class = Civil_Feature_Work_CategorySerializer




# # Viewsets for Our Services Section
# class Civil_Our_ServicesFilter(django_filters.FilterSet):
#     title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
#     tags = django_filters.CharFilter(field_name='tags', lookup_expr='icontains')
#     description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')
#     class Meta:
#         model = Civil_Our_Services
#         fields = []

# class Civil_Our_ServicesViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = Civil_Our_Services.objects.all()
#     serializer_class = Civil_Our_ServicesSerializer
#     parser_classes = [MultiPartParser]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_class = Civil_Our_ServicesFilter
    
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
# class Civil_Order_Card_Filter(django_filters.FilterSet):
#     title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
#     class Meta:
#         model = Civil_Order_Card
#         fields = []

# class Civil_Order_CardViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = Civil_Order_Card.objects.all()
#     serializer_class = Civil_Order_CardSerializer
#     parser_classes = [MultiPartParser]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_class = Civil_Order_Card_Filter
    
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         search_query = self.request.query_params.get('search', None)
#         if search_query:
#             queryset = queryset.filter(
#                 Q(title__icontains=search_query)
#             )
#         return queryset
    

# # Viewsets for Security Page Section
# class Civil_Security_PageViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = Civil_Security_Page.objects.all()
#     serializer_class = Civil_Security_PageSerializer




# # ============Viewsets for Website Notice Board Section Start============
# class Civil_Notice_BoardFilter(django_filters.FilterSet):
#     title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
#     date = django_filters.DateFilter(field_name='date', lookup_expr='icontains')
#     status = django_filters.CharFilter(field_name='status', lookup_expr='icontains')
#     class Meta:
#         model = Civil_Notice_Board
#         fields = []

# class Civil_Notice_BoardViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = Civil_Notice_Board.objects.all()
#     serializer_class = Civil_Notice_BoardSerializer
#     parser_classes = [MultiPartParser]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_class = Civil_Notice_BoardFilter
    
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
# class Civil_CompanyMemberFilter(django_filters.FilterSet):
#     name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
#     title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
#     email = django_filters.CharFilter(field_name='email', lookup_expr='icontains')
#     phone_number = django_filters.CharFilter(field_name='phone_number', lookup_expr='icontains')
#     address = django_filters.CharFilter(field_name='address', lookup_expr='icontains')
#     class Meta:
#         model = Civil_Company_Member
#         fields = []

# class Civil_Company_MemberViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = Civil_Company_Member.objects.all()
#     serializer_class = Civil_Company_MemberSerializer
#     parser_classes = [MultiPartParser]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_class = Civil_CompanyMemberFilter
    
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         search_query = self.request.query_params.get('search', None)
#         if search_query:
#             queryset = queryset.filter(
#                 Q(name__icontains=search_query) |
#                 Q(title__icontains=search_query) |
#                 Q(email__icontains=search_query) |
#                 Q(phone_number__icontains=search_query) |
#                 Q(address__icontains=search_query)
#             )
#         return queryset

# # ============Viewsets for Website Company Member Section End============




# # ============Footer Section Viewsets End============
# # Viewsets for Office Address Section
# class Civil_Office_AddressViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = Civil_Office_Address.objects.all()
#     serializer_class = Civil_Office_AddressSerializer

# # Viewsets for Payment Logo Section
# class Civil_Payment_LogoViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = Civil_Payment_Logo.objects.all()
#     serializer_class = Civil_Payment_LogoSerializer
#     parser_classes = [MultiPartParser]

# # Viewsets for Social Media Section
# class Civil_Social_MediaViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = Civil_Social_Media.objects.all()
#     serializer_class = Civil_Social_MediaSerializer
#     parser_classes = [MultiPartParser]

# # Viewsets for Subscription Section
# class Civil_SubscriptionsViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = Civil_Subscriptions.objects.all()
#     serializer_class = Civil_SubscriptionsSerializer



# # Viewsets for Footer Section
# class CivilFooterSectionTopicsViewSet(viewsets.ModelViewSet):
#     queryset = Civil_Footer_Section_Topics.objects.all()
#     serializer_class = CivilFooterSectionTopicsSerializer

# class CivilFooterSection1ViewSet(viewsets.ModelViewSet):
#     queryset = Civil_Footer_Section_1.objects.all()
#     serializer_class = CivilFooterSection1Serializer

# class CivilFooterSection2ViewSet(viewsets.ModelViewSet):
#     queryset = Civil_Footer_Section_2.objects.all()
#     serializer_class = CivilFooterSection2Serializer

# class CivilFooterSection3ViewSet(viewsets.ModelViewSet):
#     queryset = Civil_Footer_Section_3.objects.all()
#     serializer_class = CivilFooterSection3Serializer

# # ============Footer Section Viewsets End============




def test_socket(request):
    return render(request, 'test-socket.html',{})


