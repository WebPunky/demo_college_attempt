from django import forms
from django.forms import widgets
from django.utils import timezone

from .models import Orders, Review


class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ("scheduled_at", "service",)
        widgets = {
            "scheduled_at": forms.DateTimeInput(attrs={"type": "date"})
        }

    def clean_sheduled_at(self):
        value = self.cleaned_data["scheduled_at"]
        if value < timezone.now():
            raise forms.ValidationError("Нельзя выбрать прошедшую дату")
        return value

class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("rating", "comment")
        widgets = {
            "rating": forms.NumberInput(attrs={"min": 1, "max": 5}),
        }