from django.contrib import admin

# Register your models here.
from .models import Shipment, ShipmentEvent


class ShipmentEventInline(admin.TabularInline):
    model = ShipmentEvent
    extra = 1
    readonly_fields = ("timestamp",)


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ("tracking_number", "customer", "service_type", "status", "recipient_name", "created_at")
    list_filter = ("status", "service_type", "created_at")
    search_fields = ("tracking_number", "customer__username", "customer__email", "sender_name", "recipient_name")
    readonly_fields = ("tracking_number", "created_at", "updated_at")
    inlines = [ShipmentEventInline]
    actions = [
        "mark_confirmed", "mark_picked_up", "mark_in_transit",
        "mark_out_for_delivery", "mark_delivered", "mark_cancelled",
    ]

    fieldsets = (
        ("Tracking", {"fields": ("tracking_number", "customer", "service_type", "status", "assigned_driver")}),
        ("Sender", {"fields": ("sender_name", "sender_phone", "pickup_address")}),
        ("Recipient", {"fields": ("recipient_name", "recipient_phone", "delivery_address")}),
        ("Location (auto-geocoded, editable)", {
            "fields": (("pickup_latitude", "pickup_longitude"), ("delivery_latitude", "delivery_longitude"))
        }),
        ("Package", {"fields": ("item_description", "weight_kg", "special_instructions", "preferred_date", "estimated_cost")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )
    def _bulk_update_status(self, request, queryset, status, label):
        for shipment in queryset:
            shipment.status = status
            shipment.save()
        self.message_user(request, f"{queryset.count()} shipment(s) marked as {label}.")

    def mark_confirmed(self, request, queryset):
        self._bulk_update_status(request, queryset, Shipment.STATUS_CONFIRMED, "Confirmed")
    mark_confirmed.short_description = "Mark selected as Confirmed"

    def mark_picked_up(self, request, queryset):
        self._bulk_update_status(request, queryset, Shipment.STATUS_PICKED_UP, "Picked Up")
    mark_picked_up.short_description = "Mark selected as Picked Up"

    def mark_in_transit(self, request, queryset):
        self._bulk_update_status(request, queryset, Shipment.STATUS_IN_TRANSIT, "In Transit")
    mark_in_transit.short_description = "Mark selected as In Transit"

    def mark_out_for_delivery(self, request, queryset):
        self._bulk_update_status(request, queryset, Shipment.STATUS_OUT_FOR_DELIVERY, "Out for Delivery")
    mark_out_for_delivery.short_description = "Mark selected as Out for Delivery"

    def mark_delivered(self, request, queryset):
        self._bulk_update_status(request, queryset, Shipment.STATUS_DELIVERED, "Delivered")
    mark_delivered.short_description = "Mark selected as Delivered"

    def mark_cancelled(self, request, queryset):
        self._bulk_update_status(request, queryset, Shipment.STATUS_CANCELLED, "Cancelled")
    mark_cancelled.short_description = "Mark selected as Cancelled"


@admin.register(ShipmentEvent)
class ShipmentEventAdmin(admin.ModelAdmin):
    list_display = ("shipment", "status", "location", "timestamp")
    list_filter = ("status",)