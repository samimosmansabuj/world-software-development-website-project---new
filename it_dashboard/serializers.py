from rest_framework import serializers
from .models import *

# Serializers for Website Logo Section
class IT_WebsiteLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_WebsiteLogo
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website Banner Section
class IT_WebsiteBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_WebsiteBanner
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')



class ITTwoCardCustomerFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_TwoCardCustomerFeedback
        fields = '__all__'

class ITThreeCardSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_ThreeCardSection
        fields = '__all__'

class ITFourCardSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_FourCardSection
        fields = '__all__'



# Serializers for Website Template Card Section
class IT_CardTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_CardTemplate
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website Blog Card Section
class IT_BlogCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_BlogCard
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website Timedata Section
class IT_TimeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_TimeData
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website Segment Section
class IT_Homepage_SegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Homepage_Segment
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website Company Logo Section
class IT_Support_Company_LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Support_Company_Logo
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Global Location Section
class IT_Global_LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Global_Location
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Contact Section
class IT_Contact_UsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Contact_Us
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')



# Serializers for Technology Section
class IT_Technology_IconSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Technology_Icon
        fields = ('id', 'title', 'icon')

class IT_TechnologySerializer(serializers.ModelSerializer):
    all_technologies = serializers.SerializerMethodField()
    class Meta:
        model = IT_Technology
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

    def get_all_technologies(self, obj):
        icons = obj.technologies.all()
        return IT_Technology_IconSerializer(icons, many=True).data



# Serializers for Our Services Section
class IT_Our_ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Our_Services
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Notice Board Section
class IT_Notice_BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Notice_Board
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Order Card Section
class IT_Order_CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Order_Card
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


# Serializers for Security Page Section
class IT_Security_PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Security_Page
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Company Member Section
class IT_Company_MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Company_Member
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')




# Serializers for Office Address Section
class IT_Office_AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Office_Address
        fields = '__all__'

# Serializers for Payment Logo Section
class IT_Payment_LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Payment_Logo
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Social Media Section
class IT_Social_MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Social_Media
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Subscription Section
class IT_SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Subscriptions
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')




# Serializers for Footer Section
class ITFooterSectionTopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Footer_Section_Topics
        exclude = ['created_at', 'last_update_at']

class ITFooterSection1Serializer(serializers.ModelSerializer):
    all_topics = serializers.SerializerMethodField()
    class Meta:
        model = IT_Footer_Section_1
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')
    
    def get_all_topics(self, obj):
        topic = obj.topics.all()
        return ITFooterSectionTopicsSerializer(topic, many=True).data


class ITFooterSection2Serializer(serializers.ModelSerializer):
    all_topics = serializers.SerializerMethodField()
    class Meta:
        model = IT_Footer_Section_2
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')
    
    def get_all_topics(self, obj):
        topic = obj.topics.all()
        return ITFooterSectionTopicsSerializer(topic, many=True).data

class ITFooterSection3Serializer(serializers.ModelSerializer):
    all_topics = serializers.SerializerMethodField()
    class Meta:
        model = IT_Footer_Section_3
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')
    
    def get_all_topics(self, obj):
        topic = obj.topics.all()
        return ITFooterSectionTopicsSerializer(topic, many=True).data



