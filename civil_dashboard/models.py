from django.conf import settings
from django.db import models

class CivilMetaField(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['created_at']


# =================Website Logo Section Start=======================
class Civil_WebsiteLogo(CivilMetaField):
    image = models.ImageField(upload_to='civil/image/logo/',blank=True, null=True)
    def __str__(self):
        return f"{self.image.name}"
# =================Website Logo Section End=======================


# =================Website Banner Section Start=======================
class Civil_WebsiteBanner(CivilMetaField):
    header = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    image_and_video = models.FileField(upload_to='civil/image/banners/', blank=True, null=True)

    def __str__(self):
        return f"{self.header} - {self.tag}"
# =================Website Banner Section End=======================



# =================Website 2 Card Section Start=======================
class Civil_TwoCardCustomerFeedback(CivilMetaField):
    icon = models.ImageField(upload_to='civil/image/two-card-customer-feedback/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"

# =================Website 2 Card Section End=======================


# =================Website Three Card Section Start=======================
class Civil_ThreeCardSection(CivilMetaField):
    icon = models.ImageField(upload_to='civil/image/three-card-icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

# =================Website Three Card Section End=======================


# =================Website Four Card Section Start=======================
class Civil_FourCardSection(CivilMetaField):
    icon = models.ImageField(upload_to='civil/image/four-card-icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

# =================Website Four Card Section End=======================


# =================Website Template Card Section Start=======================
class Civil_CardTemplate(CivilMetaField):
    image = models.ImageField(upload_to='civil/image/template-card/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=5)
    url = models.URLField()
    
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"
# =================Website Template Card Section End=======================


# =================Website Blog Card Section Start=======================
class Civil_BlogCard(CivilMetaField):
    image = models.ImageField(upload_to='civil/image/blog-card/',blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField()
    
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"
# =================Website Blog Card Section End=======================

# =================Website Timedata Section Start=======================
class Civil_TimeData(CivilMetaField):
    year = models.PositiveSmallIntegerField()
    month = models.PositiveSmallIntegerField()
    day = models.PositiveSmallIntegerField()
    hour = models.PositiveSmallIntegerField()
    second = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day} {self.hour}:{self.second}"
# =================Website Timedata Section End=======================

# =================Website Segment Section Start=======================
class Civil_Homepage_Segment(CivilMetaField):
    photo_or_video = models.FileField(upload_to='civil/image/segment/', blank=True, null=True)
    
    def __str__(self) -> str:
        return self.photo_or_video.name
# =================Website Segment Section End=======================


# =================Website Company Logo Section Start=======================
class Civil_Support_Company_Logo(CivilMetaField):
    logo = models.ImageField(upload_to='civil/image/comapny-logo/', blank=True, null=True)
    
    def __str__(self) -> str:
        return self.logo.name
# =================Website Company Logo Section End=======================


# =================Website Global Location Section Start=======================
class Civil_Global_Location(CivilMetaField):
    flag_logo = models.ImageField(upload_to='civil/image/global-location-flag/', blank=True, null=True)
    country_name = models.CharField(max_length=30)
    office_address = models.CharField(max_length=400)
    contact_details = models.CharField(max_length=400)
    
    is_active = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.country_name
# =================Website Global Location Section End=======================

# =================Website Contact Section Start=======================
class Civil_Contact_Us(CivilMetaField):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    phone_number = models.CharField(max_length=15)
    subject = models.CharField(max_length=600)
    message = models.TextField()
    
    def __str__(self) -> str:
        return f'{self.name} - {self.email}'
# =================Website Contact Section End=======================



# ===========================Arcitecture Start=================================
class Civil_Arcitecture_Images(CivilMetaField):
    image = models.ImageField(upload_to='civil/image/arcitecture-image/', blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.image.name}'

class Civil_Arcitecture(CivilMetaField):
    title = models.CharField(max_length=150)
    feature_image = models.ManyToManyField(Civil_Arcitecture_Images)
    plan_details = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    describtion = models.TextField()
    
    def __str__(self) -> str:
        return self.title

# ===========================Arcitecture End=================================

# ===========================Freature Workd Start=================================
class Civil_Feature_Work_Category(CivilMetaField):
    title = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return f'{self.title}'

class Civil_Feature_Work(CivilMetaField):
    category = models.ForeignKey(Civil_Feature_Work_Category, on_delete=models.CASCADE, related_name='feature_work_category')
    image = models.ImageField(upload_to='civil/image/feature-work-image/', blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.category.title} - {self.image.name}'

# ===========================Freature Workd End=================================




# ===========================Our Services Start=================================
class Civil_Our_Services(CivilMetaField):
    icon = models.ImageField(upload_to='civil/image/services-icons/', blank=True, null=True)
    title = models.CharField(max_length=500)
    tags = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    is_active = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title
# ===========================Our Services End=================================


# ===========================Notice Board Start=================================
class Civil_Notice_Board(CivilMetaField):
    STATUS = (
        ('Pending', 'Pending'),
        ('Active', 'Active'),
        ('Deactivate', 'Deactivate'),
        ('Expired', 'Expired'),
    )
    title = models.CharField(max_length=500)
    date = models.DateField()
    status = models.CharField(max_length=50, choices=STATUS, default='Active')
    file = models.FileField(upload_to='civil/file/notice-board/', blank=True, null=True)
    
    is_active = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f'{self.date} - {self.title}'
# ===========================Notice Board End=================================


# ===========================Order Card Start=================================
class Civil_Order_Card(CivilMetaField):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='civil/image/order-card/', blank=True, null=True)
    file = models.FileField(upload_to='civil/file/order-card/', blank=True, null=True)
    
    is_active = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title
# ===========================Order Card End=================================


# ===========================Security Page Model Start=================================
class Civil_Security_Page(CivilMetaField):
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.description
# ===========================Security Page Model End=================================


# ===========================Company Member Start=================================
class Civil_Company_Member(CivilMetaField):
    image = models.ImageField(upload_to='civil/image/company-member/', blank=True, null=True)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    email = models.EmailField(max_length=150)
    phone_number = models.CharField(max_length=14)
    address = models.CharField(max_length=500)
    
    def __str__(self) -> str:
        return self.name
# ===========================Company Member End=================================



# =================Tow Office Address Section Models Start=======================
class Civil_Office_Address(CivilMetaField):
    address = models.CharField(max_length=500)
    email = models.EmailField(max_length=140)
    phone = models.CharField(max_length=14)
    fax = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return f'{self.address}'

# =================Tow Office Address Section Models End=======================

# =================Website Payment Logo Section Start=======================
class Civil_Payment_Logo(CivilMetaField):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='civil/image/payment-logo/', blank=True, null=True)

    def __str__(self) -> str:
        return self.name
# =================Website Payment Logo Section End=======================

# =================Website Social Media Section Start=======================
class Civil_Social_Media(CivilMetaField):
    name = models.CharField(max_length=150)
    icon = models.ImageField(upload_to='civil/image/social-media-icon/', blank=True, null=True)
    url = models.URLField(max_length=500)
    
    def __str__(self) -> str:
        return self.name
# =================Website Social Media Section End=======================


# =================Website Subscription Section Start=======================
class Civil_Subscriptions(CivilMetaField):
    email = models.EmailField(max_length=150)
    
    def __str__(self) -> str:
        return self.email
# =================Website Subscription Section End=======================



# ===========================Footer Section Start=================================
class Civil_Footer_Section_Topics(CivilMetaField):
    title = models.CharField(max_length=50)
    topic_url = models.URLField()
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)


class Civil_Footer_Section_1(CivilMetaField):
    title = models.CharField(max_length=50)
    topics = models.ManyToManyField(Civil_Footer_Section_Topics)
    
    def __str__(self) -> str:
        return self.title

class Civil_Footer_Section_2(CivilMetaField):
    title = models.CharField(max_length=50)
    topics = models.ManyToManyField(Civil_Footer_Section_Topics)
    
    def __str__(self) -> str:
        return self.title

class Civil_Footer_Section_3(CivilMetaField):
    title = models.CharField(max_length=50)
    topics = models.ManyToManyField(Civil_Footer_Section_Topics)
    
    def __str__(self) -> str:
        return self.title

# ===========================Footer Section End=================================







class Civil_ChatMessage(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='civil_sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='civil_received_messages', on_delete=models.CASCADE)
    message = models.TextField()
    flag = models.CharField(max_length=255, default="Flag")
    admin_flag = models.CharField(max_length=255, default="Flag")
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

class Civil_CallRecording(models.Model):
    caller = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='civil_call_recordings_made', on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='civil_call_recordings_received', on_delete=models.CASCADE)
    recording = models.FileField(upload_to='static/call_recordings/')
    duration = models.DurationField()
    timestamp = models.DateTimeField(auto_now_add=True)
    flag = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Call from {self.caller} to {self.receiver} on {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        ordering = ['-timestamp']    


