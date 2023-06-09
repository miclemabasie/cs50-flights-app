from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    pilot = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    origin = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="departures"
    )
    destination = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="arrivals"
    )
    duration = models.IntegerField()

    def __str__(self):
        return f"<Flight: {self.id}: {self.origin} to {self.destination}>"


class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(
        Flight,
        blank=True,
        related_name="passengers",
    )

    def __str__(self):
        return f"{self.first} {self.last}"
