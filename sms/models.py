
# Create your models here.

from django.db import models
from tenants.models import Tenant

class SMSLog(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="PENDING")

    def __str__(self):
        return f"SMS to {self.tenant} - {self.status}"

