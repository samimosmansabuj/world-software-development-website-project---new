from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from django.contrib.auth import login, logout
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import *
from .serializers import *
from .forms import *
import random
from templatetags.custom_template_tags import *
from rest_framework_simplejwt.tokens import RefreshToken
from permissions.permissions import IsAdmin


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Admin User List': reverse('user-list', request=request, format=format),
        'admin login': reverse('api-admin-login', request=request, format=format),
        'admin login otp verification': reverse('admin-login-otp-verification', request=request, format=format),
        
        'admin forget password': reverse('api-admin-forget-password', request=request, format=format),
        'admin reset password': reverse('api-admin-reset-password', request=request, format=format),
        
        'admin change password': reverse('admin-change-password-api', request=request, format=format),
    })


class AdminUserCreationAPI(generics.ListCreateAPIView):
    queryset = Admin_User.objects.all()
    serializer_class = AdminUserCreationSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = serializer.save()
        token = user.user_authentication.token if hasattr(user, 'user_authentication') and hasattr(user.user_authentication, 'token') else None
        return Response({
            'user': serializer.data,
            'token': token
        }, status=status.HTTP_201_CREATED)

class AdminUserUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin_User.objects.all()
    serializer_class = AdminUserCreationSerializer

class AdminLogin(APIView):
    serializer_class = AdminLoginSerializer
    def post(self, request, token=None, *args, **kwargs):
        serializer = AdminLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            admin_user = Admin_User.objects.get(username=username)
            
            if admin_user.user_authentication.token == token:
                otp = admin_user.admin_otp.otp
                
                otp_mail(admin_user, otp, subject = 'OTP for Login Your Account!',  status="")
                
                return Response({'message': 'OTP sent successfully'}, status=status.HTTP_200_OK)
                
            else:
                return Response({'message': 'Invalid Token!'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class AdminLoginOTPVerification(APIView):
    serializer_class = AdminOTPVerificationSerializer
    def post(self, request, *args, **kwargs):
        serializer = AdminOTPVerificationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data.get('user')
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'Account successfully verified.',
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       

# ==========User Login API End==========




# ==========Password Reset API Views Start==========
class EmailUser:
    def __init__(self, email):
        self.email = email
class AdminForgetPasswordAPIView(APIView):
    serializer_class = AdminForgetPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={})
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.context['otp'] 
            user = EmailUser(email=email)
            otp_mail(user, otp, subject = 'OTP for Password Reset!',  status="")
            return Response({"message": "OTP sent successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminResetPasswordAPIView(APIView):
    serializer_class = AdminResetPasswordSerializer
    def post(self, request, *args, **kwargs):
        serializer = AdminResetPasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            # user = get_object_or_404(Admin_User, email=request.session.get('admin_reset_password_email'))
            user = serializer.context.get('user')
            new_password = serializer.validated_data['password1']
            user.set_password(new_password)
            user.save()
            return Response({"message": "Password reset successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ==========Password Reset API Views End==========


# ==========Password Change API Views Start==========
class AdminChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = AdminChangePasswordSerializer
    def post(self, request, *args, **kwargs):
        serializer = AdminChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            form = AdminChangePasswordForm(request.user, data=serializer.validated_data)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                return Response({'detail': 'Password changed successfully!'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': form.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
# ==========Password Change API Views End==========


# ==========Admin view Delete Requests==========
class ListDeleteRequestUsers(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    def get(self, request, format=None):
        users = Custom_User.objects.filter(request_delete=True, is_superuser=False, is_staff=False) 
        serializer = UserSerializer(users, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK) 


######Approve Delete Request####### 
class ApproveUserProfileDeleteRequestAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request, pk=None):  # username argument from the URL
        # Fetch the user to be deleted. Adjust accordingly if using user ID.
        user = get_object_or_404(User, pk=pk)

        serializer = ApproveUserProfileDeleteRequestSerializer(user, data={}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Delete Request Approved. Account will be taken down in 30 days'}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
######ADMIN#######    

