# Generated by Django 5.0.7 on 2024-09-30 10:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("FitProfile", "0006_login_otp"),
    ]

    operations = [
        migrations.AddField(
            model_name="login",
            name="date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
