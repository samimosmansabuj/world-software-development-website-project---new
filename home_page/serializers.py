from rest_framework import serializers
from .models import *
from .application_form_models import OrderApplicationForm

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
        request = self.context.get('request')
        icons = obj.technology_icons.all()
        icons_data = TechnologyIconSerializer(icons, many=True, context={'request': request}).data
        for icon_data in icons_data:
            icon_data['icon'] = request.build_absolute_uri(icon_data['icon'])
        return icons_data



# ===========================Only For Civil Start=================================
class Civil_Arcitecture_ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Arcitecture_Images
        fields = ('id', 'image')
        read_only_fields = ('created_at', 'last_update_at')

from django.conf import settings
class Civil_ArcitectureSerializer(serializers.ModelSerializer):
    feature_images = serializers.SerializerMethodField()
    class Meta:
        model = Civil_Arcitecture
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')
    
    
    def get_feature_images(self, obj):
        request = self.context.get('request')
        images = obj.feature_image.all()
        images_data = Civil_Arcitecture_ImagesSerializer(images, many=True, context={'request': request}).data
        for image_data in images_data:
            image_data['image'] = request.build_absolute_uri(image_data['image'])
        return images_data
    
    # def get_feature_images(self, obj):
    #     images = obj.feature_image.all()
    #     return Civil_Arcitecture_ImagesSerializer(images, many=True).data


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
# ===========================Only For Civil Start=================================




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





class OrderApplicationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderApplicationForm
        exclude = ['user']
    
    def create(self, validated_data):
        user = self.context['request'].user
        order_application_form = OrderApplicationForm.objects.create(user=user, **validated_data)
        return order_application_form








