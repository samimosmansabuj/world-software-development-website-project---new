from typing import Iterable
from django.contrib.auth.tokens import default_token_generator
from django.dispatch import receiver
from django.db.models.signals import post_save
from account.models import Custom_User
from django.db import models

from django.utils import timezone
import datetime


# ==============================Model For Admin & Sub-Admin==================================
class Admin_User(Custom_User):
    USER_TYPE = (
        ('Admin', 'Admin'),
        ('Sub-Admin', 'Sub-Admin'),
    )
    name = models.CharField(max_length=100, blank=True, null=True)
    user_type = models.CharField(choices=USER_TYPE, blank=True, null=True, max_length=50)
    
    is_ti = models.BooleanField(default=False)
    is_civil = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if self.user_type == 'Admin':
            self.is_staff = True
            self.is_superuser = True
            self.is_ti = True
            self.is_civil = True
        elif self.user_type == 'Sub-Admin':
            self.is_staff = False
            self.is_superuser = False
        super(Admin_User, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.username


class Admin_User_Authentication_Model(models.Model):
    user = models.OneToOneField(Admin_User, on_delete=models.CASCADE, related_name='user_authentication')
    login_url = models.URLField(blank=True, null=True)
    otp = models.CharField(max_length=6)
    token = models.CharField(max_length=400)
    
    def save(self, *args, **kwargs):
        token = default_token_generator.make_token(self.user)
        self.token = token
        self.login_url = f'http://127.0.0.1:8000/admin-user/login/{token}/'
        super(Admin_User_Authentication_Model, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f'{self.user} - {self.login_url}'

@receiver(post_save, sender=Admin_User)
def create_user_authentication_model(sender, instance, created, **kwargs):
    if created:
        Admin_User_Authentication_Model.objects.create(user=instance)


class Admin_OTP(models.Model):
    admin = models.OneToOneField(Admin_User, on_delete=models.CASCADE, related_name='admin_otp')
    otp = models.IntegerField(null=True, blank=True)
    otp_expiry = models.DateTimeField(null=True, blank=True)
    OTP_TYPE = (
        ('Password', 'Password'),
        ('Login', 'Login'),
    )
    otp_type = models.CharField(choices=OTP_TYPE, blank=True, null=True, max_length=50, default='Login')

    def set_otp(self, otp, type):
        self.otp = otp
        self.otp_type = type
        self.otp_expiry = timezone.now() + datetime.timedelta(minutes=5)  # OTP expires in 5 minutes
        self.save()

    def verify_otp(self, otp, type):    
        if timezone.now() <= self.otp_expiry and self.otp == otp and self.otp_type == type:
            self.otp = None 
            self.otp_type = None
            self.save()
            return True
        return False


