from django.contrib import admin

from carwash.models import BookingStatus, CarWashPlace, Booking, CarWashService  # , DailySlotsAvailability

class BookingAdmin(admin.ModelAdmin):
    list_display = ["id", "date", "customer", "carwash", "status"]

    search_fields = ["carwash__name", "status__status", "customer__username", 'date']
    filter_horizontal = ()
    list_filter = ("date", "carwash", "status", "customer")
    fieldsets = ()


class BookingStatusAdmin(admin.ModelAdmin):
    list_display = ["id", "status"]

    search_fields = ["status"]
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class CarWashPlaceAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "services_count", "slots", "slots_last_refresh"]

    search_fields = ["name"]
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    def services_count(self, obj):
        return obj.services.count()

class CarWashServiceAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price"]

    search_fields = ["name", "price"]
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# class DailySlotsAvailabilityAdmin(admin.ModelAdmin):
#     list_display = ["id", "day", "slots"]
#     search_fields = ["day", "slots"]
#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()

admin.site.register(Booking, BookingAdmin)
admin.site.register(BookingStatus, BookingStatusAdmin)
admin.site.register(CarWashPlace, CarWashPlaceAdmin)
admin.site.register(CarWashService, CarWashServiceAdmin)
# admin.site.register(DailySlotsAvailability, DailySlotsAvailabilityAdmin)