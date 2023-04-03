from django import forms
from .models import Flight, Airport, Passenger


class BookFlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ["origin", "destination"]
