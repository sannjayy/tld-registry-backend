from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Whois, Domain
# Register your models here.

@admin.register(Domain)
class DomainAdmin(ImportExportModelAdmin):
    list_display = ['user', 'name', 'comment', 'level', 'nameservers', 'is_public', 'is_active', 'updated_at', 'created_at']

@admin.register(Whois)
class WhoisAdmin(ImportExportModelAdmin):
    list_display = ['domain', 'whois_type', 'name', 'email', 'phone', 'address', 'city', 'state', 'country', 'postal_code', 'is_active', 'updated_at', 'created_at']