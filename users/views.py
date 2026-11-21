from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login

from .models import Users
from .forms import RegisterForm

def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/hero/")

    form = RegisterForm()

    return render(request, "users/register.html", {"form": form})

    