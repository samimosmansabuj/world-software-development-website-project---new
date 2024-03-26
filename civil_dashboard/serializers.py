from rest_framework import serializers
from .models import *

# Serializers for Website Logo Section
class Civil_WebsiteLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_WebsiteLogo
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website Banner Section
class Civil_WebsiteBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_WebsiteBanner
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')




# Serializers for Website 2 Card Section
class CivilTwoCardCustomerFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_TwoCardCustomerFeedback
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website 3 Card Section
class CivilThreeCardSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_ThreeCardSection
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website 4 Card Section
class CivilFourCardSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_FourCardSection
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')





# Serializers for Website Template Card Section
class Civil_CardTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_CardTemplate
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website Blog Card Section
class Civil_BlogCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_BlogCard
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website Timedata Section
class Civil_TimeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_TimeData
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website Segment Section
class Civil_Homepage_SegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Homepage_Segment
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website Company Logo Section
class Civil_Support_Company_LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Support_Company_Logo
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Global Location Section
class Civil_Global_LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Global_Location
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Contact Section
class Civil_Contact_UsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Contact_Us
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')




# Serializers for Architecture Section
class Civil_Arcitecture_ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Arcitecture_Images
        exclude = ['created_at', 'last_update_at']

class Civil_ArcitectureSerializer(serializers.ModelSerializer):
    feature_images = serializers.SerializerMethodField()
    class Meta:
        model = Civil_Arcitecture
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')
    
    def get_feature_images(self, obj):
        feature_image = obj.feature_image.all()
        return Civil_Arcitecture_ImagesSerializer(feature_image, many=True).data


# Serializers for Feature Work Section
class Civil_Feature_Work_CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Feature_Work_Category
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

class Civil_Feature_WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Feature_Work
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')




# Serializers for Our Services Section
class Civil_Our_ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Our_Services
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Notice Board Section
class Civil_Notice_BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Notice_Board
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Order Card Section
class Civil_Order_CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Order_Card
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


# Serializers for Security Page Section
class Civil_Security_PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Security_Page
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Company Member Section
class Civil_Company_MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Company_Member
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Office Address Section
class Civil_Office_AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Office_Address
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Payment Logo Section
class Civil_Payment_LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Payment_Logo
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Social Media Section
class Civil_Social_MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Social_Media
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


# Serializers for Subscription Section
class Civil_SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Subscriptions
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')



# Serializers for Footer Section
class CivilFooterSectionTopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Footer_Section_Topics
        exclude = ['created_at', 'last_update_at']

class CivilFooterSection1Serializer(serializers.ModelSerializer):
    all_topics = serializers.SerializerMethodField()
    class Meta:
        model = Civil_Footer_Section_1
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')
    
    def get_all_topics(self, obj):
        topic = obj.topics.all()
        return CivilFooterSectionTopicsSerializer(topic, many=True).data

class CivilFooterSection2Serializer(serializers.ModelSerializer):
    all_topics = serializers.SerializerMethodField()
    class Meta:
        model = Civil_Footer_Section_2
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')
    
    def get_all_topics(self, obj):
        topic = obj.topics.all()
        return CivilFooterSectionTopicsSerializer(topic, many=True).data

class CivilFooterSection3Serializer(serializers.ModelSerializer):
    all_topics = serializers.SerializerMethodField()
    class Meta:
        model = Civil_Footer_Section_3
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')
    
    def get_all_topics(self, obj):
        topic = obj.topics.all()
        return CivilFooterSectionTopicsSerializer(topic, many=True).data

