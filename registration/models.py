from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.models import User,AbstractUser

from django.contrib.auth.models import User
from django.db import models

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=255)
    intent = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    reference_id = models.CharField(max_length=255)
    currency_code = models.CharField(max_length=3)
    amount_value = models.DecimalField(max_digits=10, decimal_places=2)
    payee_email_address = models.EmailField()
    payee_merchant_id = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    address_line_1 = models.CharField(max_length=255)
    admin_area_2 = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    country_code = models.CharField(max_length=2)
    capture_id = models.CharField(max_length=255)
    capture_status = models.CharField(max_length=255)
    capture_amount_currency_code = models.CharField(max_length=3)
    capture_amount_value = models.DecimalField(max_digits=10, decimal_places=2)
    final_capture = models.BooleanField()
    seller_protection_status = models.CharField(max_length=255)
    dispute_categories = models.JSONField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    payer_given_name = models.CharField(max_length=255)
    payer_surname = models.CharField(max_length=255)
    payer_email_address = models.EmailField()
    payer_id = models.CharField(max_length=255)
    payer_country_code = models.CharField(max_length=2)
    links_href = models.URLField()
    links_rel = models.CharField(max_length=255)
    links_method = models.CharField(max_length=10)


