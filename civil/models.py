from django.db import models
from account.models import Custom_User
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from .payment_method_models import *


# ==================================================
# Civil Order Models Section Start
# ==================================================
class Civil_Order(models.Model):
    PIORITY = (
        ('Normal', 'Normal'),
        ('Medium', 'Medium'),
        ('Emergency', 'Emergency'),
    )
    STATUS = (
        ('Pending', 'Pending'),
        ('Payment', 'Payment'),
        ('Waiting', 'Waiting'),
        ('Working', 'Working'),
        ('Complited', 'Complited'),
        ('Cancel', 'Cancel'),
    )
    CURRENCY = (
        ('USD', 'USD'),
        ('BDT', 'BDT'),
        ('INR', 'INR'),
        ('EUR', 'EUR'),
        ('GBP', 'GBP'),
        ('CAD', 'CAD'),
    )
    
    user = models.ForeignKey(Custom_User, on_delete=models.CASCADE, related_name='civil_user_order')
    project_name = models.CharField(max_length=300)
    project_file = models.FileField(upload_to='civil/order/project-file/', blank=True, null=True)
    related_file = models.FileField(upload_to='civil/order/related-file/', blank=True, null=True)
    user_information_form  = models.FileField(upload_to='civil/order/user-information-form/', blank=True, null=True)
    
    status = models.CharField(max_length=40, choices=STATUS, default='Pending')
    piority = models.CharField(max_length=40, choices=PIORITY, default='Normal')
    currency = models.CharField(max_length=20, blank=True, null=True, choices=CURRENCY)
    
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_online_deposite = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_offline_deposite = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_amount_paid = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_amount_remain = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    profit_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    delivery_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.total_amount:
            self.total_amount = 0
        if not self.total_online_deposite:
            self.total_online_deposite = 0
        if not self.total_offline_deposite:
            self.total_offline_deposite = 0
        if not self.profit_amount:
            self.profit_amount = 0
        
        self.total_amount_paid = self.total_offline_deposite + self.total_online_deposite
        self.total_amount_remain = self.total_amount - self.total_amount_paid
        
        super(Civil_Order, self).save(*args, **kwargs)

    class Meta:
        ordering = ['last_update_at', 'created_at', 'delivery_date']
    
    def __str__(self) -> str:
        return f'{self.user.username} - {self.project_name}'


class Civil_Order_Work_Document(models.Model):
    order = models.ForeignKey(Civil_Order, on_delete=models.CASCADE, related_name='civil_order_work_document')
    text_box = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.order} {self.text_box}'

class Civil_Order_Admin_Note(models.Model):
    order = models.ForeignKey(Civil_Order, on_delete=models.CASCADE, related_name='civil_order_note')
    text_box = models.TextField()
    file_or_image = models.FileField(upload_to='civil/order/note-file/', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.order} | {self.text_box}'

# ==================================================
# Civil Order Models Section End
# ==================================================





# ==================================================
# Civil Order Payment Section Start
# ==================================================
class Civil_Payment(models.Model):
    PAYMENT_TYPE = (
        ('Online', 'Online'), ('Offline', 'Offline')
    )
    PAYMENT_METHOD = (
        ('Bank', 'Bank'), ('Mobile', 'Mobile')
    )
    
    order = models.ForeignKey(Civil_Order, on_delete=models.CASCADE, related_name='civil_order_payment')
    
    currency = models.CharField(max_length=3, choices=(('USD', 'USD'), ('BDT', 'BDT')), blank=True, null=True)
    payment_amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_type = models.CharField(max_length=10, choices=PAYMENT_TYPE)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD, blank=True, null=True)
    is_varified = models.BooleanField(default=False)
    is_refund = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    paymend_added = models.BooleanField(default=False)
    
    bank = models.ForeignKey(Civil_Bank, on_delete=models.DO_NOTHING, related_name='civil_bank', blank=True, null=True)
    mobile_wallet = models.ForeignKey(Civil_MobileWallet, on_delete=models.DO_NOTHING, related_name='civil_mobile_wallet', blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs) -> None:
        if self.order.currency:
            self.currency = self.order.currency
        
        if self.is_varified == True and self.status == True and self.paymend_added == False:
            payment_order = self.order
            if self.payment_type == 'Online':
                payment_order.total_online_deposite += self.payment_amount
            else:
                payment_order.total_offline_deposite += self.payment_amount
            self.paymend_added = True
            payment_order.save()
        
        super(Civil_Payment, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f'{self.order.project_name} - {self.pk}'


class Civil_BankPayment(models.Model):
    payment = models.OneToOneField(Civil_Payment, on_delete=models.CASCADE, related_name='bank_payment')
    
    account_holder_name = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100, blank=False)
    account_number = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=100, unique=True)
    transaction_receipt = models.ImageField(upload_to='civil/image/transaction_receipts/', blank=True, null=True)
    additional_info = models.TextField(blank=True)
    
    def __str__(self) -> str:
        return f'{self.payment.order.project_name} - {self.pk}'
    
class Civil_MobilePayment(models.Model):
    payment = models.OneToOneField(Civil_Payment, on_delete=models.CASCADE, related_name='mobile_payment')
    
    account_holder_name = models.CharField(max_length=100)
    mobile_wallet_name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=100)
    transaction_id = models.CharField(max_length=100, unique=True)
    transaction_receipt = models.ImageField(upload_to='civil/image/transaction_receipts/', blank=True, null=True)

    
    def __str__(self) -> str:
        return f'{self.payment.order.project_name} - {self.pk}'

class Civil_OfflinePayment(models.Model):
    payment = models.OneToOneField(Civil_Payment, on_delete=models.CASCADE, related_name='offline_payment')
    
    country_name = models.CharField(max_length=100)
    receipt_person_name = models.CharField(max_length=100)
    receipt_person_id = models.CharField(max_length=100)
    
    check_holder_name = models.CharField(max_length=100)
    check_holder_phone_number = models.CharField(max_length=14)
    check_number = models.CharField(max_length=100)
    check_security_code = models.CharField(max_length=100)
    check_receipt = models.FileField(upload_to='civil/image/check_receipt/', blank=True, null=True)
    
    is_varified = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs) -> None:
        civil_offline_payment_check = Civil_OfflineCheck.objects.filter(
            payment_receipt_person_id=self.receipt_person_id,
            check_holder_phone_number = self.check_holder_phone_number,
            check_number = self.check_number,
            check_security_code = self.check_security_code,
        ).exists()
        if civil_offline_payment_check:
            self.is_varified = True
        else:
            self.is_varified = False
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.check_holder_name} - {self.check_number} - {self.receipt_person_name} - {self.payment.pk}"

# ==================================================
# Civil Order Payment Section End
# ==================================================


# ==================================================
# Civil Order Refund Section Start
# ==================================================

class Civil_Refund(models.Model):
    REFUND_METHOD = (
        ('Bank', 'Bank'),
        ('Mobile', 'Mobile')
    )
    STATUS = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Complete', 'Complete'),
        ('Cancel', 'Cancel')
    )
    order = models.ForeignKey(Civil_Order, on_delete=models.CASCADE, related_name='order_refund')
    payment = models.OneToOneField(Civil_Payment, on_delete=models.CASCADE, related_name='payment_refund')
    
    refund_method = models.CharField(max_length=50, choices=REFUND_METHOD, blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True, editable=False)
    refund_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, editable=False)
    status = models.CharField(max_length=50, choices=STATUS, default='Pending')
    
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    preferred_contact_method = models.CharField(max_length=20, blank=True, null=True)
    
    reason_for_refund = models.TextField()
    proof_of_payment = models.FileField(upload_to='civil/image/refund_proofs/', blank=True, null=True)
    additional_notes = models.TextField(blank=True, null=True)
    special_instructions = models.TextField(blank=True, null=True)
    feedback_or_suggestions = models.TextField(blank=True, null=True)
    documentation_or_evidence = models.FileField(upload_to='civil/image/refund_documents/', blank=True, null=True)
    specific_issue_details = models.TextField(blank=True, null=True)
    additional_comments = models.TextField(blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    paymend_added = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f'{self.order.pk} | {self.payment.pk} | {self.name} | {self.email}'
    
    def save(self, *args, **kwargs):
        if self.payment.payment_type == 'Online':
            self.refund_method = self.payment.payment_method
        self.currency = self.payment.currency
        self.refund_amount = self.payment.payment_amount
        
        if self.status == 'Complete' and self.paymend_added == False:
            refund_payment = self.payment
            refund_payment.is_refund = True
            refund_payment.status = False
            refund_payment.save()
            
            refund_payment_order = refund_payment.order
            if refund_payment.payment_type == 'Online':
                refund_payment_order.total_online_deposite -= refund_payment.payment_amount
            elif refund_payment.payment_type == 'Offline':
                refund_payment_order.total_offline_deposite -= refund_payment.payment_amount
            refund_payment_order.save()
            self.paymend_added = True
        
        super(Civil_Refund, self).save(*args, **kwargs)

class Civil_Bank_Refund(models.Model):
    refund = models.OneToOneField(Civil_Refund, on_delete=models.CASCADE, related_name="civil_bank_refund")
    
    recipient_bank_name = models.CharField(max_length=100)
    recipient_bank_account_name = models.CharField(max_length=100)
    recipient_bank_account_number = models.CharField(max_length=100)
    recipient_bank_routing_name = models.CharField(max_length=100)
    iban_or_swift_code = models.CharField(max_length=100)
    account_info = models.TextField()
    additional_info = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.refund.pk} | {self.recipient_bank_name} | {self.recipient_bank_account_name} | {self.recipient_bank_account_number}'


class Civil_Mobile_Refund(models.Model):
    refund = models.OneToOneField(Civil_Refund, on_delete=models.CASCADE, related_name="civil_mobile_refund")
    
    recipient_mobile_wallet_name = models.CharField(max_length=100)
    recipient_wallet_account_name = models.CharField(max_length=100)
    recipient_wallet_account_number = models.CharField(max_length=100)
    account_info = models.TextField()
    additional_info = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.refund.pk} | {self.recipient_mobile_wallet_name} | {self.recipient_wallet_account_name} | {self.recipient_wallet_account_number}'

# ==================================================
# Civil Order Refund Section End
# ==================================================



