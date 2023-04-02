from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    template_name = 'flights/lists.html'
    flights = []

    context = {
            'flights': flights,
            'flight_list_active': True
        }
    return HttpResponse("<h1>This is some testing </h1>")
    # return render(request, template_name, context)
