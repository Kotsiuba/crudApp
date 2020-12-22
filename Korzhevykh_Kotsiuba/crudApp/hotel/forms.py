from django import forms
from hotel.models import Hotel, Tour


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = "__all__"


class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = "__all__"
