# Generated by Django 4.2.2 on 2023-06-24 15:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("registration", "0007_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscription",
            name="address_line_1",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="admin_area_2",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="amount_value",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="capture_amount_currency_code",
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="capture_amount_value",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="capture_id",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="capture_status",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="country_code",
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="create_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="currency_code",
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="dispute_categories",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="final_capture",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="full_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="intent",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="links_href",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="links_method",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="links_rel",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="payee_email_address",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="payee_merchant_id",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="payer_country_code",
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="payer_email_address",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="payer_given_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="payer_id",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="payer_surname",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="payment_id",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="postal_code",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="reference_id",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="seller_protection_status",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="status",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="update_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
