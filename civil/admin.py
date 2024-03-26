from django.contrib import admin
from .models import *

@admin.register(Civil_Order)
class Civil_OrderAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'status', 'piority', 'currency', 'total_amount', 'total_amount_paid', 'total_amount_remain', 'delivery_date')
    list_filter = ('status', 'piority', 'currency', 'delivery_date', 'created_at', 'last_update_at')
    search_fields = ('user__name', 'project_name', 'status', 'piority', 'currency')

@admin.register(Civil_Order_Work_Document)
class Civil_Order_Work_DocumentAdmin(admin.ModelAdmin):
    list_display = ('order', 'text_box', 'url', 'last_update_at')
    list_filter = ('created_at', 'last_update_at')
    search_fields = ('order__user__name', 'text_box')


@admin.register(Civil_Order_Admin_Note)
class Civil_OrderAdminNoteAdmin(admin.ModelAdmin):
    list_display = ('order', 'text_box', 'file_or_image', 'last_update_at')
    list_filter = ('created_at', 'last_update_at')
    search_fields = ('order__user__name', 'text_box')


