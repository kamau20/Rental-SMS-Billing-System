# Create your models here.

from django.db import models
from tenants.models import Tenant

class MonthlyBill(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    month = models.IntegerField()
    year = models.IntegerField()

    garbage_fee = models.DecimalField(max_digits=10, decimal_places=2)
    water_bill = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return self.tenant.monthly_rent + self.garbage_fee + self.water_bill

    @property
    def balance(self):
        return self.total - self.amount_paid

    def __str__(self):
        return f"{self.tenant} ({self.month}/{self.year})"

