from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import update_session_auth_hash
from .forms import ChangePasswordForm
from django.db import IntegrityError

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from rest_framework_simplejwt.exceptions import TokenError
from account.models import *
from rest_framework.decorators import api_view, permission_classes
User = get_user_model()

from templatetags.custom_template_tags import *
from permissions.permissions import IsVerifiedUser



class LoginAPIView(APIView):
    serializer_class = UserLoginSerializer
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'username': user.username,
                'email': user.email,
            })

        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)      

class UserRegistrationAPIView(APIView):
    serializer_class = UserRegistrationSerializer
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            otp = user.otp.otp
  
            otp_mail(user, otp, subject = 'OTP for Account Verification!', status='')

            return Response({
                'user': serializer.data['username'],
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': 'Please verify your account using the OTP sent to your email.'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def verify_otp(request):
    user = request.user
    otp = request.data.get('otp')
    if user.otp.verify_otp(int(otp), type="Login"):
        return Response({'message': 'Account successfully verified.'})
    else:
        return Response({'error': 'Invalid or expired OTP.'}, status=status.HTTP_400_BAD_REQUEST)

  
@api_view(['POST'])
def regenerate_otp(request):
    serializer = RegenerateOTPSerializer(data=request.data)
    
    if serializer.is_valid():
        validated_data = serializer.save()  # Regenerate OTP
        user = validated_data['user']
        new_otp = validated_data['new_otp']

        # Generate a new token for the user
        refresh = RefreshToken.for_user(user)
                
        otp_mail(user, new_otp, subject = 'OTP for Account Verification!', status="new")

        return Response({
            'message': 'OTP regenerated and sent successfully.',
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        })
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      

class DeleteProfileRequestAPIView(APIView):
    permission_classes = [IsAuthenticated, IsVerifiedUser]

    def delete(self, request):
        user = request.user
        serializer = DeleteProfileRequestSerializer(user, data={}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Success! Account will be deleted 30 days after admin approval.'}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class CancelDeleteProfileRequestAPIView(APIView):
    permission_classes = [IsAuthenticated, IsVerifiedUser]
    def post(self, request):
        user = request.user
        serializer = CancelDeleteProfileRequestSerializer(user, data={}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Delete request cancelled'}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated, IsVerifiedUser]

    def post(self, request):
        print(request.data)
        try:
            # Assuming the refresh token is sent in the body of the request
            refresh_token = request.data.get('refresh_token')
            if refresh_token is None:
                return Response({"error": "Refresh token not provided."}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"message": f"Logged out successfully"}, status=status.HTTP_205_RESET_CONTENT)
        except TokenError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated, IsVerifiedUser]
    def get(self, request):
        user_profile = get_object_or_404(Custom_User, username=request.user.username)
        serializer = CustomUserProfileSerializer(user_profile)
        return Response(serializer.data)
    
    def put(self, request):
        try:
            user_instance = request.user
        except Custom_User.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CustomUserProfileSerializer(user_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# =============== Views For Website User Profile ===================
# class UserProfileAPI(viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin):
#     permission_classes = [IsAuthenticated, IsVerifiedUser]
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer
    
#     def get_queryset(self):
#         return self.queryset.filter(user=self.request.user)
    
#     def perform_update(self, serializer):
#         serializer.save(user=self.request.user)


class UserProfileAPI(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsVerifiedUser]

    def get_object(self):
        return self.request.user.user_profile

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

# =========== Views For Website User Company Information ===============
class CompanyInformatinoAPI(generics.CreateAPIView, generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CompanyInformationSerializer
    
    def get_object(self):
        try:
            return self.request.user.user_company_information
        except CompanyInformation.DoesNotExist:
            return None
    
    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except IntegrityError:
            return Response({"error": "A company information object already exists for this user."},
                            status=status.HTTP_400_BAD_REQUEST)

# ================= Views For Website User Address =====================
class AddressAPI(generics.CreateAPIView, generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, IsVerifiedUser]
    serializer_class = AddressSerializer
    
    def get_object(self):
        try:
            return self.request.user.user_address
        except Address.DoesNotExist:
            return None
    
    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except IntegrityError:
            return Response({"error": "A company information object already exists for this user."},
                            status=status.HTTP_400_BAD_REQUEST)

# ================ Views For Website User Social Link ====================
class SocialLinkAPI(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsVerifiedUser]
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer
    
    def get_queryset(self):
        return SocialLink.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


# class CompanyInformationViewsets(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = CompanyInformation.objects.all()
#     serializer_class = CompanyInformationSerializer

#     def get_queryset(self):
#         # try:
#         #     return CompanyInformation.objects.filter(user=self.request.user)
#         # except CompanyInformation.DoesNotExist:
#         #     return CompanyInformation.objects.none()
#         return CompanyInformation.objects.filter(user=self.request.user)
        

#     def perform_create(self, serializer):
#         try:
#             serializer.save(user=self.request.user)
#         except IntegrityError:
#             return Response({"error": "A company information object already exists for this user."},
#                             status=status.HTTP_400_BAD_REQUEST)

#     # def perform_update(self, serializer):
#     #     serializer.save(user=self.request.user)




# ==========Password Change API Views Start==========
class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            form = ChangePasswordForm(request.user, data=serializer.validated_data)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                return Response({'detail': 'Password changed successfully!'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': form.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
# ==========Password Change API Views End==========

 
class EmailUser:
    def __init__(self, email):
        self.email = email
class ForgetPasswordAPIView(APIView):
    serializer_class = ForgetPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={})
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.context['otp'] 
            user = EmailUser(email=email)
            otp_mail(user, otp, subject = 'OTP for Password Reset!',  status="")
            return Response({"message": "OTP sent successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordAPIView(APIView):
    serializer_class = ResetPasswordSerializer
    def post(self, request, *args, **kwargs):
        serializer = ResetPasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.context.get('user')
            new_password = serializer.validated_data['password1']
            user.set_password(new_password)
            user.save()
            return Response({"message": "Password reset successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       
# ==========Password Reset API Views End==========




