from django.views.generic import TemplateView
from django.shortcuts import render
from hotel.models import Hotel


class ShowHotelsView(TemplateView):
    template_name = 'showHotels.html'

    def get(self, request, *args, **kwargs):
        hotels = Hotel.objects.all()
        return render(request, self.template_name, {'hotels': hotels})
