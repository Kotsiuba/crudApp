from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View
from django.shortcuts import render, redirect

from hotel.forms import HotelForm

class AddHotelView(PermissionRequiredMixin, View):
    template_name = 'addHotel.html'
    permission_required = 'hotel.add_tour'

    def get(self, request, *args, **kwargs):
        form = HotelForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = HotelForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show/hotels')
            except:
                pass

        return render(request, self.template_name, {'form': form})
