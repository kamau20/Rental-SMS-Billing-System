
# Create your models here.

from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    house_number = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.house_number}"

