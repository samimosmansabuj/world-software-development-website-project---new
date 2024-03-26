from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from .models import *
from django.core.validators import MinLengthValidator
import random
from django.contrib.auth import get_user_model
User = get_user_model()

# ==========Admin User Creation Serializer Start==========
class AdminUserCreationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[MinLengthValidator(1, "Name cannot be blank")])
    user_type = serializers.ChoiceField(
        choices=[('Admin', 'Admin'), ('Sub-Admin', 'Sub-Admin')],
        validators=[MinLengthValidator(1, "User Type cannot be blank")]
    )
    is_civil = serializers.CharField()
    is_ti = serializers.CharField()

    password1 = serializers.CharField(write_only=True, required=False, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=False, style={'input_type': 'password'})

    class Meta:
        model = Admin_User
        fields = ['id', 'name', 'email', 'username', 'user_type', 'is_civil', 'is_ti', 'password1', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }
        
    def validate_is_civil(self, value):
        if value == 'Yes':
            return True
        elif value == 'No':
            return False
        else:
            raise serializers.ValidationError("This field must be either 'Yes' or 'No'.")

    def validate_is_ti(self, value):
        if value == 'Yes':
            return True
        elif value == 'No':
            return False
        else:
            raise serializers.ValidationError("This field must be either 'Yes' or 'No'.")

    
    def validate_password1(self, value):
        validate_password(value)
        return value

    def validate(self, data):
        if 'password1' in data and 'password2' in data and data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        user = Admin_User.objects.create(
            name=validated_data['name'],
            email=validated_data['email'],
            username=validated_data['username'],
            user_type=validated_data['user_type'],
            is_civil=validated_data['is_civil'],
            is_ti=validated_data['is_ti']
        )
        user.set_password(validated_data['password1'])
        user.save()
        user.token = user.user_authentication.token
        return user
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.user_type = validated_data.get('user_type', instance.user_type)
        instance.is_civil = validated_data.get('is_civil', instance.is_civil)
        instance.is_ti = validated_data.get('is_ti', instance.is_ti)

        password1 = validated_data.get('password1')
        password2 = validated_data.get('password2')

        if password1 and password2:
            if password1 != password2:
                raise serializers.ValidationError("Passwords do not match.")
            instance.set_password(password1)
        instance.save()
        return instance
    
    # ==========Admin User Creation Serializer End==========


# ==========User Login Serializer Start==========
class AdminLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        user = Admin_User.objects.filter(username=username).first()
    
        if user:
            auth_user = authenticate(username=username, password=password)
            if auth_user:
                # Generate a random 6-digit OTP
                otp = random.randint(100000, 999999)
                if hasattr(user, 'admin_otp'):
                    user.admin_otp.set_otp(otp, type='Login')
                else:
                   Admin_OTP.objects.create(admin=user, otp=otp, otp_type='Login',otp_expiry=timezone.now() + datetime.timedelta(minutes=5))
                return data
            else:
                raise serializers.ValidationError("Invalid Password!")
        else:
            raise serializers.ValidationError("Invalid Username!")


class AdminOTPVerificationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    otp = serializers.IntegerField()

    def validate(self, data):
        username = data.get('username')
        otp = data.get('otp')

        # Check if admin exists
        try:
            user = User.objects.get(username=username)    
        except User.DoesNotExist:
            raise serializers.ValidationError({"username": "Invalid username. This user does not exist."}) 
        
        if hasattr(user.admin_user, 'admin_otp') and user.admin_user.admin_otp.verify_otp(otp, type="Login"):
            # If the OTP verification is successful, attach the user to the data
            data['user'] = user
        else:
            raise serializers.ValidationError({'otp': 'Invalid or expired OTP.'})

        return data       
  
# ==========User Login Serializer End==========


# ==========Password Reset Serializer Start==========
class AdminForgetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('context', {})
        super(AdminForgetPasswordSerializer, self).__init__(*args, **kwargs)

    def validate_email(self, value):
        # Check if the email exists in the database
        admin_user = Admin_User.objects.filter(email=value).first()
        if not admin_user:
            raise serializers.ValidationError("Email does not exist in our database.")
        # If email exists, generate OTP
        otp = random.randint(100000, 999999)
        if hasattr(admin_user, 'admin_otp'):
            admin_user.admin_otp.set_otp(otp, type='Password')
        else:
            Admin_OTP.objects.create(admin=admin_user, otp=otp,otp_type='Password',otp_expiry=timezone.now() + datetime.timedelta(minutes=5))             
        self.context['otp'] = otp
        return value

    def create(self, validated_data):
        validated_data['otp'] = self.otp
        return validated_data
    


    
    
class AdminResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.IntegerField()
    password1 = serializers.CharField(label='New Password', write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(label='New Confirm Password', write_only=True, style={'input_type': 'password'})

    def validate_email(self, value):
        # Check if the user exists through the email
        try:
            user = Admin_User.objects.get(email=value)
            self.context['user'] = user
        except Admin_User.DoesNotExist:
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
        if not (hasattr(user, 'admin_otp') and user.admin_otp.verify_otp(otp_to_verify, type="Password")):
            raise serializers.ValidationError("Invalid or expired OTP.")
       
        return data
# ==========Password Reset Serializer End==========


# ==========Password Change Serializer Views Start==========
class AdminChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    new_password1 = serializers.CharField(label='New Password', write_only=True, style={'input_type': 'password'})
    new_password2 = serializers.CharField(label='New Confirm Password', write_only=True, style={'input_type': 'password'})
# ==========Password Change Serializer Views End==========


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom_User  # Use your actual user model here
        fields = ['id', 'username', 'email', 'request_delete']  # Add fields you want to include in your API response


######Approve delete request#########
class ApproveUserProfileDeleteRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['is_deleted','deleted_date']
        read_only_fields = ['is_deleted', 'deleted_date']
    
    def update(self, instance, validated_data):
        if instance.request_delete == False:
            raise serializers.ValidationError("No Delete Request was made for this user")
    
        if instance.is_deleted == True:
            raise serializers.ValidationError("Delete request already approved")

        instance.is_deleted = True
        instance.deleted_date = timezone.now()
        instance.save()
        return instance      
######Approve delete request#########