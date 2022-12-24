from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model


class BookingStatus(models.Model):
    status = models.CharField(max_length=40, verbose_name="status")

    def __repr__(self):
        return self.status

    def __str__(self):
        return self.status

    def __unicode__(self):
        return self.status


class CarWashService(models.Model):
    name = models.CharField(max_length=40, verbose_name="carwash service")
    price = models.IntegerField(verbose_name="price", default=100)

    def __repr__(self):
        return self.name

    def __str__(self):
        return f"{self.name} costs {self.price}"

    def __unicode__(self):
        return self.name


class CarWashPlace(models.Model):
    name = models.CharField(verbose_name="carwash name", max_length=160)
    services = models.ManyToManyField(CarWashService, verbose_name="services")
    slots = models.IntegerField(default=5, verbose_name='slots available today')

    slots_last_refresh = models.DateField(default=now(), verbose_name='slots refreshed on')

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Booking(models.Model):
    customer = models.ForeignKey(
        get_user_model(), verbose_name="customer", on_delete=models.SET_NULL, null=True
    )
    carwash = models.ForeignKey(
        CarWashPlace, verbose_name="carwash place", on_delete=models.SET_NULL, null=True
    )

    service = models.ForeignKey(CarWashService, verbose_name="services", null=True, on_delete=models.DO_NOTHING)

    status = models.ForeignKey(
        BookingStatus, verbose_name="booking status", on_delete=models.DO_NOTHING, null=True,
    )

    date = models.DateField(blank=True, null=True, default=now)

    def __unicode__(self):
        return self._id

    def __str__(self):
        return f"Booking for {self.customer.username} on {self.date} at {self.carwash.name} is {self.status.status}"

