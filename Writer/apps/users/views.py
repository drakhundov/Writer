from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User


def register(request):
    return render(request, "users/register.html")


def save_users(request):
    User.objects.create_user(request.POST["username"],
                             request.POST["mail"],
                             request.POST["password"])
    
    return HttpResponseRedirect(reverse("articles:last"))