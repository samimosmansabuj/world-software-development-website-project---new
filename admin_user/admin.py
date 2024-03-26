from django.contrib import admin
from .models import *

@admin.register(Admin_User)
class Custom_User_Admin(admin.ModelAdmin):
    list_display = ['email', 'username', 'user_type', 'update_date']
    list_filter = ['user_type']
    search_fields = ['email', 'username', 'user_type']


admin.site.register(Admin_User_Authentication_Model)
