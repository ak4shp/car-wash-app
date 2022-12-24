# Generated by Django 4.1.1 on 2022-12-24 00:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("carwash", "0005_alter_booking_date_remove_carwashplace_services_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="service",
            field=models.ManyToManyField(
                null=True, to="carwash.carwashservice", verbose_name="services"
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="date",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(2022, 12, 24, 6, 5, 22, 903890),
                null=True,
            ),
        ),
    ]