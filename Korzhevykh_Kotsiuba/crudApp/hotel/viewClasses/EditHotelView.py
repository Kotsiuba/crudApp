from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View
from django.shortcuts import render, redirect

from hotel.models import Hotel
from hotel.forms import HotelForm

class EditHotelView(PermissionRequiredMixin, View):
    template_name = 'editHotel.html'
    permission_required = 'hotel.change_hotel'

    def get(self, request, *args, **kwargs):
        hotel = Hotel.objects.get(id=kwargs['id'])
        return render(request, self.template_name, {'hotel': hotel})

    def post(self, request, *args, **kwargs):
        hotel = Hotel.objects.get(id=kwargs['id'])
        form = HotelForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            return redirect("/show/hotels")
        return render(request, self.template_name, {'hotel': hotel})

