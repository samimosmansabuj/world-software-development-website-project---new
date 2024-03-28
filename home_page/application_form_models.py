from django.db import models
from account.models import Custom_User

class OrderApplicationForm(models.Model):
    SECTION = (
        ('IT', 'IT'),
        ('Civil', 'Civil')
    )
    section = models.CharField(max_length=10, choices=SECTION)
    # Personal Information
    user = models.ForeignKey(Custom_User, on_delete=models.CASCADE, related_name='user_order_application_form')
    full_name = models.CharField(max_length=50)
    photo = models.ImageField()
    fathers_name = models.CharField(max_length=50)
    mothers_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    MARITAL_STATUS_CHOICES = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    )
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES)
    religion = models.CharField(max_length=50)
    speaking_language = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    month_salary = models.DecimalField(max_digits=10, decimal_places=2)
    nationality = models.CharField(max_length=50)
    national_id_or_passport_number = models.CharField(max_length=50)
    
    # Permanent Address
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state_or_province = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    address = models.TextField(blank=True, null=True)
    
    # Contact Information
    cell_phone_number = models.CharField(max_length=20)
    fax_number = models.CharField(max_length=20)
    email_address = models.EmailField()
    
    # Project Creation Requirements
    PROJECT_TYPE_CHOICES = (
        ('Personal', 'Personal'),
        ('Company', 'Company'),
        ('Government', 'Government'),
    )
    project_type = models.CharField(max_length=10, choices=PROJECT_TYPE_CHOICES)
    technology_used = models.CharField(max_length=100)
    colors_used = models.CharField(max_length=100)
    project_deadline = models.DateField()
    project_description = models.TextField(blank=True, null=True)
    additional_information = models.TextField(blank=True, null=True)
    
    # Company Information
    company_name = models.CharField(max_length=50)
    company_type = models.CharField(max_length=50)
    company_phone_number = models.CharField(max_length=20)
    company_email_address = models.EmailField()
    company_location_address = models.TextField()
    company_website_url = models.URLField()
    
    # Signatures
    project_manager_signature = models.CharField(max_length=255)
    applicant_signature = models.CharField(max_length=255)
    
    agree = models.BooleanField(default=False)
    
    def __str__(self):
        return self.full_name


