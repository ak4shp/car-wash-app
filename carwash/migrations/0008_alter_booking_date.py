# Generated by Django 4.1.1 on 2022-12-24 00:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("carwash", "0007_alter_booking_date_remove_booking_service_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="date",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2022, 12, 24, 6, 10, 14, 570106),
                null=True,
            ),
        ),
    ]