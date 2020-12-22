from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from hotel.forms import HotelForm, TourForm
from hotel.models import Hotel, Tour
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.forms import EmailField
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



def index(request):
    return render(request, "index.html")

def destroyHotel(request, id):
    try:
        hotel = Hotel.objects.get(id=id)
        hotel.delete();
    except:
        pass
    return redirect("/show/hotels")


def destroyTour(request, id):
    tour = Tour.objects.get(id=id)
    tour.delete()
    return redirect("/show/tours")

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("/show/hotels")
        else:
            return render(request, 'registration/register.html', {'form': form})
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def contacts(request):
    return render(request, "contacts.html")

def custom404(request, exception, template_name='404.html'):
    response = render(request, template_name)
    response.status_code = 404
    return response

def notFound(request):
    response = render(request, '404.html')
    return response































class CustomUserCreationForm(UserCreationForm):
    email = EmailField(label=_("Email address"), required=True, help_text=_("Required."))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
