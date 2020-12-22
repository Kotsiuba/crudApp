from django.views import View
from django.shortcuts import render

from hotel.models import Tour


class ShowToursView(View):
    template_name = 'showTours.html'

    def get(self, request, *args, **kwargs):
        tours = Tour.objects.all()
        return render(request, self.template_name, {'tours': tours})
