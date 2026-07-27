

# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ShipmentRequestForm, TrackingForm
from .models import Shipment


@login_required
def create_shipment(request):
    if request.method == "POST":
        form = ShipmentRequestForm(request.POST)
        if form.is_valid():
            shipment = form.save(commit=False)
            shipment.customer = request.user
            shipment.save()
            messages.success(
                request,
                f"Delivery request submitted! Your tracking number is {shipment.tracking_number}."
            )
            return redirect("shipping:shipment_detail", tracking_number=shipment.tracking_number)
    else:
        initial = {
            "sender_name": request.user.full_name,
            "sender_phone": request.user.phone_number,
            "pickup_address": request.user.home_address,
        }
        form = ShipmentRequestForm(initial=initial)
    return render(request, "shipping/create_shipment.html", {
        "form": form, "page_title": "Request a Delivery"
    })


@login_required
def dashboard(request):
    shipments = request.user.shipments.all()
    return render(request, "shipping/dashboard.html", {
        "shipments": shipments, "page_title": "My Shipments"
    })


@login_required
def shipment_detail(request, tracking_number):
    shipment = get_object_or_404(
        Shipment, tracking_number=tracking_number, customer=request.user
    )
    return render(request, "shipping/shipment_detail.html", {
        "shipment": shipment, "page_title": f"Shipment {shipment.tracking_number}"
    })


def track_shipment(request):
    shipment = None
    searched = False
    if request.method == "POST":
        form = TrackingForm(request.POST)
        if form.is_valid():
            searched = True
            shipment = Shipment.objects.filter(
                tracking_number=form.cleaned_data["tracking_number"].strip()
            ).first()
            if not shipment:
                messages.error(request, "No shipment found with that tracking number.")
    else:
        form = TrackingForm()
    return render(request, "shipping/track.html", {
        "form": form, "shipment": shipment, "searched": searched, "page_title": "Track Your Delivery"
    })