from django.db import models

class MetaField(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['created_at']

class SectionChoice(models.TextChoices):
    IT = 'IT', 'IT'
    CIVIL = 'Civil', 'Civil'



class Logo(MetaField):
    section = models.CharField(max_length=10, choices=SectionChoice.choices)
    image = models.ImageField(upload_to='image/logo/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.section} Logo"


class Banner(MetaField):
    section = models.CharField(max_length=10, choices=SectionChoice.choices)
    header = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    image_and_video = models.FileField(upload_to='image/banners/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.section} Banner - {self.header}"

class TwoCardCustomerFeedback(MetaField):
    section = models.CharField(max_length=10, choices=SectionChoice.choices)
    icon = models.ImageField(upload_to='image/two-card-customer-feedback/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.section} Two Card - {self.title}"

class ThreeCardSection(MetaField):
    section = models.CharField(max_length=10, choices=SectionChoice.choices)
    icon = models.ImageField(upload_to='image/three-card-icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.section} Three Card - {self.title}"

class FourCardSection(MetaField):
    section = models.CharField(max_length=10, choices=SectionChoice.choices)
    icon = models.ImageField(upload_to='image/four-card-icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.section} Four Card - {self.title}"

class CardTemplate(MetaField):
    section = models.CharField(max_length=10, choices=SectionChoice.choices)
    image = models.ImageField(upload_to='image/template-card/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=5)
    url = models.URLField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.section} Template - {self.title}"

class BlogCard(MetaField):
    section = models.CharField(max_length=10, choices=SectionChoice.choices)
    image = models.ImageField(upload_to='image/blog-card/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.section} Blog Card - {self.title}"

class TimeData(MetaField):
    year = models.PositiveSmallIntegerField()
    month = models.PositiveSmallIntegerField()
    day = models.PositiveSmallIntegerField()
    hour = models.PositiveSmallIntegerField()
    second = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return f"{self.year}-{self.month}-{self.day} {self.hour}:{self.second}"

class HomepageSegment(MetaField):
    section = models.CharField(max_length=10, choices=SectionChoice.choices)
    photo_or_video = models.FileField(upload_to='image/segment/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.section} Segment"

class SupportCompanyLogo(MetaField):
    section = models.CharField(max_length=10, choices=SectionChoice.choices)
    logo = models.ImageField(upload_to='image/company-logo/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.section} Company Logo"

class GlobalLocation(MetaField):
    section = models.CharField(max_length=10, choices=SectionChoice.choices)
    flag_logo = models.ImageField(upload_to='image/global-location-flag/', blank=True, null=True)
    country_name = models.CharField(max_length=30)
    office_address = models.CharField(max_length=400)
    contact_details = models.CharField(max_length=400)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.section} Global Location - {self.country_name}"

class ContactUs(MetaField):
    section = models.CharField(max_length=10, choices=SectionChoice.choices)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    phone_number = models.CharField(max_length=15)
    subject = models.CharField(max_length=600)
    message = models.TextField()
    
    def __str__(self):
        return f"{self.section} Contact - {self.name}"


# ===========================Only For IT Start=================================
class TechnologyIcon(MetaField):
    title = models.CharField(max_length=150)
    icon = models.ImageField(upload_to='image/technology-icons/', blank=True, null=True)
    
    def __str__(self):
        return self.title

class Technology(MetaField):
    name = models.CharField(max_length=150)
    technology_icons = models.ManyToManyField(TechnologyIcon)
    
    def __str__(self):
        return f"Technology - {self.name}"
# ===========================Only For IT End=================================


# ===========================Only For Civil Start=================================
class Civil_Arcitecture_Images(MetaField):
    image = models.ImageField(upload_to='image/arcitecture-image/', blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.image.name}'

class Civil_Arcitecture(MetaField):
    title = models.CharField(max_length=150)
    feature_image = models.ManyToManyField(Civil_Arcitecture_Images)
    plan_details = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    describtion = models.TextField()
    
    def __str__(self) -> str:
        return f'Arcitecture - {self.title}'



class Civil_Feature_Work_Category(MetaField):
    title = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return f'{self.title}'

class Civil_Feature_Work(MetaField):
    category = models.ForeignKey(Civil_Feature_Work_Category, on_delete=models.CASCADE, related_name='feature_work_category')
    image = models.ImageField(upload_to='image/feature-work-image/', blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.category.title} - {self.image.name}'

# ===========================Only For Civil End=================================



class OurServices(MetaField):
    section = models.CharField(max_length=10, choices=SectionChoice.choices)
    icon = models.ImageField(upload_to='image/services-icons/', blank=True, null=True)
    title = models.CharField(max_length=500)
    tags = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.section} Service - {self.title}"

class NoticeBoard(MetaField):
    section = models.CharField(max_length=10, choices=SectionChoice.choices)
    STATUS = (
        ('Pending', 'Pending'),
        ('Active', 'Active'),
        ('Deactivate', 'Deactivate'),
        ('Expired', 'Expired'),
    )
    title = models.CharField(max_length=500)
    date = models.DateField()
    status = models.CharField(max_length=50, choices=STATUS, default='Active')
    file = models.FileField(upload_to='file/notice-board/', blank=True, null=True)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.section} Notice - {self.date} - {self.title}"

class OrderCard(MetaField):
    section = models.CharField(max_length=10, choices=SectionChoice.choices)
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='image/order-card/', blank=True, null=True)
    file = models
    
    def __str__(self):
        return f"{self.section} Order - {self.title}"


class SecurityPage(MetaField):
    section = models.CharField(max_length=10, choices=SectionChoice.choices)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.section} Security Page"

class CompanyMember(MetaField):
    section = models.CharField(max_length=10, choices=SectionChoice.choices)
    image = models.ImageField(upload_to='image/company-member/', blank=True, null=True)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    email = models.EmailField(max_length=150)
    phone_number = models.CharField(max_length=14)
    address = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.section} Company Member - {self.name}"

class OfficeAddress(MetaField):
    section = models.CharField(max_length=10, choices=SectionChoice.choices)
    address = models.CharField(max_length=500)
    email = models.EmailField(max_length=140)
    phone = models.CharField(max_length=14)
    fax = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.section} Office Address - {self.address}"

class PaymentLogo(MetaField):
    section = models.CharField(max_length=10, choices=SectionChoice.choices)
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='image/payment-logo/', blank=True, null=True)

    def __str__(self):
        return f"{self.section} Payment Logo - {self.name}"

class SocialMedia(MetaField):
    section = models.CharField(max_length=10, choices=SectionChoice.choices)
    name = models.CharField(max_length=150)
    icon = models.ImageField(upload_to='image/social-media-icon/', blank=True, null=True)
    url = models.URLField(max_length=500)

    def __str__(self):
        return f"{self.section} Social Media - {self.name}"

class Subscriptions(MetaField):
    section = models.CharField(max_length=10, choices=SectionChoice.choices)
    email = models.EmailField(max_length=150)

    def __str__(self):
        return f"{self.section} Subscription - {self.email}"

class FooterSectionTopics(MetaField):
    section = models.CharField(max_length=10, choices=SectionChoice.choices)
    title = models.CharField(max_length=50)
    topic_url = models.URLField()
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.section} Footer Topic - {self.title}"

class FooterSection1(MetaField):
    section = models.CharField(max_length=10, choices=SectionChoice.choices)
    title = models.CharField(max_length=50)
    topics = models.ManyToManyField(FooterSectionTopics)

    def __str__(self):
        return f"{self.section} Footer Section 1 - {self.title}"

class FooterSection2(MetaField):
    section = models.CharField(max_length=10, choices=SectionChoice.choices)
    title = models.CharField(max_length=50)
    topics = models.ManyToManyField(FooterSectionTopics)

    def __str__(self):
        return f"{self.section} Footer Section 2 - {self.title}"

class FooterSection3(MetaField):
    section = models.CharField(max_length=10, choices=SectionChoice.choices)
    title = models.CharField(max_length=50)
    topics = models.ManyToManyField(FooterSectionTopics)

    def __str__(self):
        return f"{self.section} Footer Section 3 - {self.title}"




