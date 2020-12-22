from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View
from django.shortcuts import render, redirect
from hotel.models import Tour, Hotel
from hotel.forms import TourForm

class EditTourView(PermissionRequiredMixin, View):
    template_name = 'editTour.html'
    id = None
    permission_required = 'hotel.change_tour'

    def get(self, request, *args, **kwargs):
        tour = Tour.objects.get(id=kwargs['id'])
        return render(request, self.template_name, {'tour': tour})

    def post(self, request, *args, **kwargs):
        tour = Tour.objects.get(id=kwargs['id'])
        try:
            hotel_name = request.POST["hotel_name"];
            updated_request = request.POST.copy()
            updated_request.update({'hotel': Hotel.objects.get(name=hotel_name)})

            form = TourForm(updated_request, instance=tour)
            if form.is_valid():
                form.save()
                return redirect("/show/tours")
        except:
            pass
        return render(request, self.template_name, {'tour': tour})

