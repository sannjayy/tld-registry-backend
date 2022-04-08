from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import ApiKey

# Admin Dashboard Texts
admin.site.site_header = "TLD Registry Admin"
admin.site.site_title = "TLD Registry Portal"
admin.site.index_title = "Welcome to TLD Registry Portal"

# Register your models here.

@admin.register(ApiKey)
class ApiKey(ImportExportModelAdmin):
    list_display = ['user', 'api_key', 'allowed_ip', 'is_active', 'updated_at', 'created_at']
    filter_horizontal = ('allowed_domains',)