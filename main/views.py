from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def hero(request: HttpRequest) -> HttpResponse:
    return render(request, "main/hero.html")