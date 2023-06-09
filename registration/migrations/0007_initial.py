# Generated by Django 4.2 on 2023-06-17 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("registration", "0006_delete_customuser"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subscription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("payment_id", models.CharField(max_length=255)),
                ("intent", models.CharField(max_length=255)),
                ("status", models.CharField(max_length=255)),
                ("reference_id", models.CharField(max_length=255)),
                ("currency_code", models.CharField(max_length=3)),
                ("amount_value", models.DecimalField(decimal_places=2, max_digits=10)),
                ("payee_email_address", models.EmailField(max_length=254)),
                ("payee_merchant_id", models.CharField(max_length=255)),
                ("full_name", models.CharField(max_length=255)),
                ("address_line_1", models.CharField(max_length=255)),
                ("admin_area_2", models.CharField(max_length=255)),
                ("postal_code", models.CharField(max_length=20)),
                ("country_code", models.CharField(max_length=2)),
                ("capture_id", models.CharField(max_length=255)),
                ("capture_status", models.CharField(max_length=255)),
                ("capture_amount_currency_code", models.CharField(max_length=3)),
                (
                    "capture_amount_value",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("final_capture", models.BooleanField()),
                ("seller_protection_status", models.CharField(max_length=255)),
                ("dispute_categories", models.JSONField()),
                ("create_time", models.DateTimeField()),
                ("update_time", models.DateTimeField()),
                ("payer_given_name", models.CharField(max_length=255)),
                ("payer_surname", models.CharField(max_length=255)),
                ("payer_email_address", models.EmailField(max_length=254)),
                ("payer_id", models.CharField(max_length=255)),
                ("payer_country_code", models.CharField(max_length=2)),
                ("links_href", models.URLField()),
                ("links_rel", models.CharField(max_length=255)),
                ("links_method", models.CharField(max_length=10)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
