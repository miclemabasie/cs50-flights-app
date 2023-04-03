from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flight, Airport, Passenger
from django.shortcuts import get_object_or_404
from .forms import BookFlightForm
from django.urls import reverse

# Create your views here.


def index(request):
    template_name = "flights/index.html"
    flights = Flight.objects.all()

    context = {
        "flights": flights,
        "flight_list_active": True,
    }

    return render(request, template_name, context)


def flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    # Get the passenger on the flight
    passengers = flight.passengers.all()
    template_name = "flights/flight.html"
    context = {
        "flight": flight,
        "passengers": passengers,
        "non_passengers": Passenger.objects.exclude(flights=flight).all(),
        "flight_detail_active": True,
    }

    return render(request, template_name, context)


def book(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    # form = BookFlightForm(request.POST or None)

    if request.method == "POST":
        passenger_id = request.POST.get("passenger")
        passenger = get_object_or_404(Passenger, id=passenger_id)
        passenger.flights.add(flight)
        print(f"Passenger: {passenger} has booked flight {flight} successfuly!")
        return HttpResponseRedirect(reverse("flights:flight", args=(flight.id,)))

    context = {
        "form": form,
    }

    template_name = "flights/book.html"

    return render(request, template_name, context)
