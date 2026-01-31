
# Register your models here.

from django.contrib import admin
from .models import Tenant

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'house_number', 'phone', 'monthly_rent')
    search_fields = ('name', 'house_number', 'phone')
