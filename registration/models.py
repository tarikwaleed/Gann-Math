from django.contrib.auth.models import User
from django.db import models


class Subscription(models.Model):
    payment_id = models.CharField(max_length=255, null=True, blank=True, default="MANUAL")
    currency_code = models.CharField(max_length=3, null=True, blank=True, default="USD")
    amount_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)  
