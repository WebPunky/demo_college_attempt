from django.urls import path

from . import views


app_name = "main"

urlpatterns = [
    path('create_order/', views.create_order, name="create_order"),
    path('list_order/', views.list_order, name="list_order"),
    path('list_order/<int:order_id>/cancel', views.cancel_order, name="cancel_order"),
    path('', views.hero, name="hero"),
]
