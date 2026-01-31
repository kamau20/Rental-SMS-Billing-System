
# Register your models here.

from django.contrib import admin
from .models import SMSLog

@admin.register(SMSLog)
class SMSLogAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'phone', 'status', 'sent_at')
    list_filter = ('status',)
