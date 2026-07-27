from django.urls import path
from . import views

app_name = "shipping"

urlpatterns = [
    path("request/", views.create_shipment, name="create_shipment"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("shipment/<str:tracking_number>/", views.shipment_detail, name="shipment_detail"),
    path("track/", views.track_shipment, name="track_shipment"),
]