from django.contrib import admin

# Register your models here.
from .models import Hotel, Tour
from django.contrib import admin
# admin.site.register(Hotel)

admin.site.site_header = 'Korzhevykh_Kotsiuba'


class TourInlineAdmin(admin.TabularInline):
    list_display = ('name', 'description')
    search_fields = ('name')
    model=Tour


class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'stars', 'description')
    search_fields = ('name', 'description')
    inlines = [TourInlineAdmin]


admin.site.register(Hotel, HotelAdmin)
