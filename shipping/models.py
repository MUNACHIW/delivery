from django.db import models

# Create your models here.
import random
import string
from django.conf import settings
from django.urls import reverse


def generate_tracking_number():
    while True:
        code = "RC" + "".join(random.choices(string.digits, k=10))
        if not Shipment.objects.filter(tracking_number=code).exists():
            return code


class Shipment(models.Model):
    SERVICE_STANDARD = "standard"
    SERVICE_EXPRESS = "express"
    SERVICE_TEMPERATURE = "temperature"
    SERVICE_HAZMAT = "hazmat"
    SERVICE_CHOICES = [
        (SERVICE_STANDARD, "Standard"),
        (SERVICE_EXPRESS, "Express"),
        (SERVICE_TEMPERATURE, "Temperature Controlled"),
        (SERVICE_HAZMAT, "Hazmat / Special"),
    ]

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_PICKED_UP = "picked_up"
    STATUS_IN_TRANSIT = "in_transit"
    STATUS_OUT_FOR_DELIVERY = "out_for_delivery"
    STATUS_DELIVERED = "delivered"
    STATUS_CANCELLED = "cancelled"
    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending Confirmation"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_PICKED_UP, "Picked Up"),
        (STATUS_IN_TRANSIT, "In Transit"),
        (STATUS_OUT_FOR_DELIVERY, "Out for Delivery"),
        (STATUS_DELIVERED, "Delivered"),
        (STATUS_CANCELLED, "Cancelled"),
    ]

    tracking_number = models.CharField(
        max_length=20, unique=True, editable=False, default=generate_tracking_number
    )
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="shipments"
    )

    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES, default=SERVICE_STANDARD)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)

    sender_name = models.CharField(max_length=150)
    sender_phone = models.CharField(max_length=20)
    pickup_address = models.TextField()

    recipient_name = models.CharField(max_length=150)
    recipient_phone = models.CharField(max_length=20)
    delivery_address = models.TextField()

    item_description = models.CharField(max_length=255)
    weight_kg = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    special_instructions = models.TextField(blank=True)

    preferred_date = models.DateField(blank=True, null=True)
    estimated_cost = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    assigned_driver = models.CharField(max_length=150, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.tracking_number} ({self.get_status_display()})"

    def get_absolute_url(self):
        return reverse("shipping:shipment_detail", args=[self.tracking_number])

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        old_status = None
        if not is_new:
            old_status = Shipment.objects.filter(pk=self.pk).values_list("status", flat=True).first()

        super().save(*args, **kwargs)

        if is_new:
            ShipmentEvent.objects.create(
                shipment=self, status=self.status, note="Delivery request received."
            )
        elif old_status and old_status != self.status:
            ShipmentEvent.objects.create(
                shipment=self, status=self.status, note=f"Status updated to {self.get_status_display()}."
            )


class ShipmentEvent(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name="events")
    status = models.CharField(max_length=20, choices=Shipment.STATUS_CHOICES)
    location = models.CharField(max_length=150, blank=True)
    note = models.CharField(max_length=255, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return f"{self.shipment.tracking_number} - {self.get_status_display()}"