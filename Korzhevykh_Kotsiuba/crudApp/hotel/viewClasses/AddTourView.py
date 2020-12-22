from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View
from django.shortcuts import render, redirect

from hotel.forms import TourForm
from hotel.models import Hotel


class AddTourView(PermissionRequiredMixin, View):
    template_name = 'addTour.html'
    id = None
    permission_required = 'hotel.add_tour'

    def get(self, request, *args, **kwargs):
        if not request.user.has_perm('hotel.add_tour'):
            perm_list = request.user.user_permissions.all().values_list('codename', flat=True)
            return redirect('/404')
        form = TourForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        updated_request = request.POST.copy()
        updated_request.update({'hotel': Hotel.objects.get(id=kwargs['id'])})

        form = TourForm(updated_request)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show/tours')
            except:
                pass

        return render(request, self.template_name, {'form': form})

