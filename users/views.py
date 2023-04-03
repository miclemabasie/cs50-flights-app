from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout


def index(request):
    template_name = "users/user.html"
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    user = request.user
    context = {
        "user": user,
        "user_active": True,
    }

    return render(request, template_name, context)


def login_view(request):
    template_name = "users/login.html"
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # Verify if user exist in the database through authentication
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("users:index"))
        else:
            print("No user with this credentials")

    return render(request, template_name)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("users:login"))
