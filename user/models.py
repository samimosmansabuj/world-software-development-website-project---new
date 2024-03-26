from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from account.models import Custom_User
from django.contrib.auth.tokens import default_token_generator

# ==============================Model For Website User==================================
class UserProfile(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    user = models.OneToOneField(Custom_User, on_delete=models.CASCADE, related_name='user_profile')
    full_name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, default="Male")
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    occupation = models.CharField(max_length=30, blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.user.username} | {self.full_name}'


@receiver(post_save, sender=Custom_User)
def create_user_authentication_profile_model(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


class CompanyInformation(models.Model):
    user = models.OneToOneField(Custom_User, on_delete=models.CASCADE, related_name='user_company_information')
    
    company_name = models.CharField(max_length=255)
    company_location = models.CharField(max_length=255)
    company_phone_number = models.CharField(max_length=20)
    company_details = models.TextField(blank=True, null=True)
    company_website = models.URLField()
    
    def __str__(self) -> str:
        return f'{self.user.username} | {self.company_name}'

class SocialLink(models.Model):
    SOCIAL_MEIDA_NAME = (
        ('Facebook', 'Facebook'),
        ('Linkedin', 'Linkedin'),
        ('Instagram', 'Instagram'),
    )
    user = models.ForeignKey(Custom_User, on_delete=models.CASCADE, related_name='user_social_link')
    icon_select = models.CharField(max_length=20, choices=SOCIAL_MEIDA_NAME)
    url = models.URLField()
    
    def __str__(self) -> str:
        return f'{self.user.username} | {self.icon_select}'

class Address(models.Model):
    user = models.OneToOneField(Custom_User, on_delete=models.CASCADE, related_name='user_address')
    street_address = models.CharField(max_length=255)
    state_province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f'{self.user.username} | {self.city}'



