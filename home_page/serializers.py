from rest_framework import serializers
from .models import *

class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


class TwoCardCustomerFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwoCardCustomerFeedback
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


class ThreeCardSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreeCardSection
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


class FourCardSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FourCardSection
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


class CardTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardTemplate
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


class BlogCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCard
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


class TimeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeData
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


class HomepageSegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomepageSegment
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


class SupportCompanyLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportCompanyLogo
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


class GlobalLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalLocation
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


class TechnologyIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologyIcon
        fields = ('id', 'title', 'icon')


class TechnologySerializer(serializers.ModelSerializer):
    technology_icon = serializers.SerializerMethodField()
    class Meta:
        model = Technology
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')
    
    def get_technology_icon(self, obj):
        icons = obj.technology_icons.all()
        return TechnologyIconSerializer(icons, many=True).data


class Civil_Arcitecture_ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Arcitecture_Images
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


class Civil_ArcitectureSerializer(serializers.ModelSerializer):
    feature_image = Civil_Arcitecture_ImagesSerializer(many=True)

    class Meta:
        model = Civil_Arcitecture
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


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


class OurServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurServices
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


class NoticeBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeBoard
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


class OrderCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCard
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


class SecurityPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityPage
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


class CompanyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyMember
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


class OfficeAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeAddress
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


class PaymentLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentLogo
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


class FooterSectionTopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterSectionTopics
        exclude = ['created_at', 'last_update_at']


class FooterSection1Serializer(serializers.ModelSerializer):
    all_topics = serializers.SerializerMethodField()
    class Meta:
        model = FooterSection1
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')
    
    def get_all_topics(self, obj):
        topic = obj.topics.all()
        return FooterSectionTopicsSerializer(topic, many=True).data


class FooterSection2Serializer(serializers.ModelSerializer):
    all_topics = serializers.SerializerMethodField()
    class Meta:
        model = FooterSection2
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')
    
    def get_all_topics(self, obj):
        topic = obj.topics.all()
        return FooterSectionTopicsSerializer(topic, many=True).data


class FooterSection3Serializer(serializers.ModelSerializer):
    all_topics = serializers.SerializerMethodField()
    class Meta:
        model = FooterSection3
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')
    
    def get_all_topics(self, obj):
        topic = obj.topics.all()
        return FooterSectionTopicsSerializer(topic, many=True).data
