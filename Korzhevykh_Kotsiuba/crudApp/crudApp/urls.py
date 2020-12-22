"""crudApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from hotel import views

from hotel.viewClasses.ShowHotelsView import ShowHotelsView
from hotel.viewClasses.EditHotelView import EditHotelView
from hotel.viewClasses.AddHotelView import AddHotelView

from hotel.viewClasses.ShowToursView import ShowToursView
from hotel.viewClasses.EditTourView import EditTourView
from hotel.viewClasses.AddTourView import AddTourView
from django.conf.urls import handler404
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('hotels', AddHotelView.as_view()),
    path('show/hotels', ShowHotelsView.as_view()),
    path('hotels/<int:id>/edit', EditHotelView.as_view()),

    path('tours/<int:id>', AddTourView.as_view()),
    path('show/tours', ShowToursView.as_view()),
    path('tours/<int:id>/edit', EditTourView.as_view()),

    path('hotels/<int:id>/delete', views.destroyHotel),
    path('tours/<int:id>/delete', views.destroyTour),

    path('contacts', views.contacts),
    path('', views.index),
    path('signup/', views.signup),
    path('404', views.notFound, ),

    path('i18n/', include('django.conf.urls.i18n')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = 'hotel.views.custom404'
handler403 = 'hotel.views.custom404'
