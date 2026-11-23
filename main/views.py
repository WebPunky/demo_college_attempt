from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Services

def hero(request: HttpRequest) -> HttpResponse:
    services = Services.objects.all()
    return render(request, "main/hero.html", {"services": services})