# Generated by Django 4.1.1 on 2022-12-24 00:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("carwash", "0010_alter_booking_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="date",
            field=models.DateField(
                blank=True, default=datetime.date(2022, 12, 24), null=True
            ),
        ),
    ]
