
# Register your models here.

from django.contrib import admin
from .models import MonthlyBill
from .services import generate_bill_sms
from sms.services import send_sms

@admin.register(MonthlyBill)
class MonthlyBillAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'month', 'year', 'total', 'amount_paid', 'balance')
    list_filter = ('month', 'year')
    actions = ['send_sms_to_tenant']

    def send_sms_to_tenant(self, request, queryset):
        for bill in queryset:
            message = generate_bill_sms(bill)
            send_sms(bill.tenant, message)

        self.message_user(request, "SMS sent successfully!")

    send_sms_to_tenant.short_description = "Send rent SMS to selected tenants"
