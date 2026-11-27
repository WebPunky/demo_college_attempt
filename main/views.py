from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.core.exceptions import PermissionDenied

from .models import Services, Orders, Review
from .forms import CreateOrderForm, CreateReviewForm


def hero(request: HttpRequest) -> HttpResponse:
    services = Services.objects.all()
    return render(request, "main/hero.html", {"services": services})

@login_required
def create_order(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect("/users/profile/")

    form = CreateOrderForm()

    return render(request, "main/create_order.html", {"form": form})

@login_required
def list_order(request: HttpRequest) -> HttpResponse:
    orders = Orders.objects.filter(user=request.user)
    return render(request, "main/list_order.html", {"orders": orders})

@login_required
@require_POST
def cancel_order(request: HttpRequest, order_id: int) -> HttpResponse:
    order = get_object_or_404(Orders, id=order_id, user=request.user)

    try:
        order.cancel()
    except ValueError as error:
        messages.error(request, str(error))
    else:
        messages.success(request, "Order was cancelled")

    return redirect("main:list_order")

@login_required
def create_review(request: HttpRequest, order_id:int) -> HttpResponse:
    order = get_object_or_404(Orders, id=order_id, user=request.user)

    if order.status != Orders.Status.DONE:
        raise PermissionDenied

    if Review.objects.filter(order=order).exists():
        return redirect("main:order_list")

    if request.method == "POST":
        form = CreateReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.order = order
            review.save()
            return redirect("main:list_order")

    form = CreateReviewForm()

    return render(request, "main/create_review.html", {"form": form, "order": order})
    