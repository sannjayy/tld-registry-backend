from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import City, State, Country
# Register your models here.

@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    list_display = ['name']

@admin.register(State)
class StateAdmin(ImportExportModelAdmin):
    list_display = ['name']

@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    list_display = ['name']