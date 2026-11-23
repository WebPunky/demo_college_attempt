from django.urls import path

from . import views


app_name = "main"

urlpatterns = [
    path('create_order/', views.create_order, name="create_order"),
    path('', views.hero, name="hero"),
]
