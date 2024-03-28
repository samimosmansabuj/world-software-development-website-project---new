from django.db import models


# ==================================================
# Website Sound System Models For Whole Website Start
# ==================================================
class SectionChoice(models.TextChoices):
    IT = 'IT', 'IT'
    CIVIL = 'Civil', 'Civil'


class Civil_Live_Chat_Admin_Sound(models.Model):
    section = models.CharField(max_length=10, choices=SectionChoice.choices)
    admin_live_chat_notification_sound = models.FileField(upload_to='civil/sound/admin_live_chat_notification_sound/', blank=True, null=True)
    admin_live_call_ringtone = models.FileField(upload_to='civil/sound/admin_live_call_ringtone/', blank=True, null=True)
    user_cannot_call_admin_sound = models.FileField(upload_to='civil/sound/user_cannot_call_admin_sound/', blank=True, null=True)
    
    def __str__(self) -> str:
        return f'Admin Live Chat Sound {self.pk}'

class Civil_User_Sound(models.Model):
    section = models.CharField(max_length=10, choices=SectionChoice.choices)
    website_entry_sound = models.FileField(upload_to='civil/sound/entry_sound/', blank=True, null=True)
    live_chat_talk_sound = models.FileField(upload_to='civil/sound/live_chat_talk_sound/', blank=True, null=True)
    live_chat_turned_off_sound = models.FileField(upload_to='civil/sound/live_chat_turned_off_sound/', blank=True, null=True)
    user_live_chat_notification_sound = models.FileField(upload_to='civil/sound/user_live_chat_notification_sound/', blank=True, null=True)
    user_live_call_ringtone = models.FileField(upload_to='civil/sound/user_live_call_ringtone/', blank=True, null=True)
    
    def __str__(self) -> str:
        return f'User Sound {self.pk}'


class Civil_User_Order_Sound(models.Model):
    section = models.CharField(max_length=10, choices=SectionChoice.choices)
    order_chat_notification_tone = models.FileField(upload_to='civil/sound/order_chat_notification_tone/', blank=True, null=True)
    order_call_ringtone = models.FileField(upload_to='civil/sound/order_call_ringtone/', blank=True, null=True)
    
    def __str__(self) -> str:
        return f'User Order Sound {self.pk}'
# ==================================================
# Website Sound System Models For Whole Website End
# ==================================================


