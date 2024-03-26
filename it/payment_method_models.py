from django.db import models

# ==================================================
# IT Payment Method Models For Whole Website Start
# ==================================================
#Bank Models-------------
class IT_Bank(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='it/image/bank_icons/', blank=True, null=True)
    qr_code = models.ImageField(upload_to='it/image/bank_qr_codes/', blank=True, null=True)
    account_details = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}-{self.icon}-{self.qr_code} {self.account_details}:{self.active}"

#Mobile Wallet Models-------------
class IT_MobileWallet(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='it/image/mobile_wallet_icons/', blank=True, null=True)
    qr_code = models.ImageField(upload_to='it/image/mobile_wallet_qr_codes/', blank=True, null=True)
    account_details = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}-{self.icon}-{self.qr_code} {self.account_details}:{self.active}"

# Offline Models-------------
class IT_OfflineCheck(models.Model):
    country_name = models.CharField(max_length=100)
    payment_receipt_person_name = models.CharField(max_length=100)
    payment_receipt_person_id = models.CharField(max_length=100)
    
    check_holder_name = models.CharField(max_length=100)
    check_holder_gmail = models.EmailField()
    check_holder_phone_number = models.CharField(max_length=14)
    check_number = models.CharField(max_length=100, unique=True)
    check_security_code = models.CharField(max_length=100, unique=True)
    currency_iso = models.CharField(max_length=3)
    check_amount = models.CharField(max_length=100)
    
    status = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ['check_number', 'check_security_code']

    def __str__(self):
        return f"{self.country_name}-{self.check_holder_name}-{self.check_number} {self.check_amount} : {self.payment_receipt_person_name}-{self.payment_receipt_person_id} {self.country_name}"

# ==================================================
# IT Payment Method Models For Whole Website End
# ==================================================

