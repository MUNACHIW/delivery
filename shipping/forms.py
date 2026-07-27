from django import forms
from .models import Shipment


class ShipmentRequestForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = [
            "service_type",
            "sender_name", "sender_phone", "pickup_address",
            "recipient_name", "recipient_phone", "delivery_address",
            "item_description", "weight_kg", "special_instructions",
            "preferred_date",
        ]
        widgets = {
            "pickup_address": forms.Textarea(attrs={"rows": 3}),
            "delivery_address": forms.Textarea(attrs={"rows": 3}),
            "special_instructions": forms.Textarea(attrs={"rows": 3}),
            "preferred_date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            css_class = "form-select" if name == "service_type" else "form-control"
            existing = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = (existing + " " + css_class).strip()


class TrackingForm(forms.Form):
    tracking_number = forms.CharField(
        max_length=20,
        label="",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. RC1234567890"}),
    )