from django.contrib import admin
from .models import Flight

# Register your models here.

class FlightAdmin(admin.ModelAdmin):
    list_display = ['origin', 'destination', 'duration']
    list_filter = ['origin', 'destination']


admin.site.register(Flight, FlightAdmin)
