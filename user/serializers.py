from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import *
from account.models import *
import random

from django.contrib.auth import get_user_model
User = get_user_model()

from django.utils.crypto import get_random_string
from django.shortcuts import get_object_or_404

from django.contrib.auth import authenticate


# # ==============================
# # Serializers For Website User Registration And Verficiation
# # ==================================





# ==========Password Change Serializer Views Start==========
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=50, write_only=True)
    new_password1 = serializers.CharField(label='New Password', max_length=50, write_only=True)
    new_password2 = serializers.CharField(label='New Confirm Password', max_length=50, write_only=True)
    
    def validate_new_password1(self, value):
        validate_password(value)
        return value    
# ==========Password Change Serializer Views End==========




# ==========Password Reset Serializer Start==========
class ForgetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('context', {})
        super(ForgetPasswordSerializer, self).__init__(*args, **kwargs)

    def validate_email(self, value):
        # Check if the email exists in the database
        user = User.objects.filter(email=value).first()
        if not user:
            raise serializers.ValidationError("Email does not exist in our database.")
        # If email exists, generate OTP
        otp = random.randint(100000, 999999)
        if hasattr(user, 'otp'):
            user.otp.set_otp(otp, type='Password')
        else:
            UserOTP.objects.create(user=user, otp=otp,otp_type='Password',otp_expiry=timezone.now() + datetime.timedelta(minutes=5))             
        self.context['otp'] = otp
        return value

    def create(self, validated_data):
        validated_data['otp'] = self.otp
        return validated_data
    

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.IntegerField()
    password1 = serializers.CharField(label='New Password', write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(label='New Confirm Password', write_only=True, style={'input_type': 'password'})

    def validate_email(self, value):
        # Check if the user exists through the email
        try:
            user = User.objects.get(email=value)
            self.context['user'] = user
        except User.DoesNotExist:
            raise serializers.ValidationError("Email does not exist.")
        return value

    def validate_otp(self, value):
        # Store the OTP in context for later verification
        self.context['otp_to_verify'] = value
        return value

    def validate_password1(self, value):
        validate_password(value)
        return value

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")

        user = self.context.get('user')
        otp_to_verify = self.context.get('otp_to_verify')
        if not (hasattr(user, 'otp') and user.otp.verify_otp(otp_to_verify, type="Password")):
            raise serializers.ValidationError("Invalid or expired OTP.")
       
        return data
# ==========Password Reset Serializer End==========



class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)

            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
            else:
                if user.is_verified == False:
                    raise serializers.ValidationError("This account is not verified!")
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        data['user'] = user
        return data

class UserRegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

    def validate_password1(self, value):
        validate_password(value)
        return value
    
    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError({"password": "The two password fields didn't match."})
        return data

    def create(self, validated_data):
        validated_data.pop('password1')
        password = validated_data.pop('password2')

        user = User.objects.create_user(password=password, **validated_data)
        otp = random.randint(111111, 999999)
        profile, created = UserOTP.objects.get_or_create(user=user)
        profile.set_otp(otp, type="Login")
        return user


class RegenerateOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, data):
        # Retrieve user by email
        user = get_object_or_404(User, email=data['email'])
        if user.is_verified == False:
            data['user'] = user
            return data
        else:
            raise serializers.ValidationError("This account is already verified!")

    def save(self, **kwargs):
        user = self.validated_data['user']
        # Generate a new OTP
        new_otp = get_random_string(length=6, allowed_chars='1234567890')
        user_otp, created = UserOTP.objects.get_or_create(user=user)
        user_otp.set_otp(new_otp, type="Login")
        self.validated_data['new_otp'] = new_otp
        return self.validated_data
    
 
class DeleteProfileRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['request_delete']
        read_only_fields = ['request_delete']
    
    def update(self, instance, validated_data):
        if instance.request_delete == True:
            raise serializers.ValidationError("Delete Already Requested!")
    
        if instance.is_deleted == True:
            raise serializers.ValidationError("Account will be deleted after within 30 days")

        instance.request_delete = True
        instance.save()
        return instance 

class CancelDeleteProfileRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['request_delete', 'is_deleted']
        read_only_fields = ['request_delete', 'is_deleted']
    
    def update(self, instance, validated_data):
    
        instance.request_delete = False
        instance.is_deleted = False
        instance.save()
        return instance      







# =============== Serializers For Website User Profile ===================
# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         exclude = ('user',)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


# =========== Serializers For Website User Company Information ===============
class CompanyInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInformation
        exclude = ('user',)


# ================ Serializers For Website User Social Link ====================
class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        exclude = ('user',)

# ================= Serializers For Website User Address =====================
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ('user',)



class CustomUserProfileSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()
    company_information = serializers.SerializerMethodField()
    social_link = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    class Meta:
        model = Custom_User
        fields = ['id', 'username', 'email', 'request_delete', 'profile', 'company_information', 'social_link', 'address']
    
    def get_profile(self, obj):
        try:
            profile = obj.user_profile
            return UserProfileSerializer(profile).data
        except UserProfile.DoesNotExist:
            return None
    
    def get_company_information(self, obj):
        try:
            company_information = obj.user_company_information
            return CompanyInformationSerializer(company_information).data
        except CompanyInformation.DoesNotExist:
            return None
    
    def get_social_link(self, obj):
        social_link = obj.user_social_link.all()
        return SocialLinkSerializer(social_link, many=True).data
    
    def get_address(self, obj):
        try:
            address = obj.user_address
            return AddressSerializer(address).data
        except Address.DoesNotExist:
            return None
    
    

