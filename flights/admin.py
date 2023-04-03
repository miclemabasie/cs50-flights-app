from django.contrib import admin
from .models import Flight, Airport, Passenger

# Register your models here.


class FlightAdmin(admin.ModelAdmin):
    list_display = ["id", "origin", "destination", "duration"]
    list_filter = ["origin", "destination"]
    list_display_links = ["id"]


admin.site.register(Flight, FlightAdmin)


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ["code", "city"]


@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ["first", "last"]
    list_display_links = ["first", "last"]
