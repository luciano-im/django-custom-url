from django.contrib import admin

from custom_url.models import CustomUrl


class CustomUrlAdmin(admin.ModelAdmin):
    list_display = ('url', 'file', 'file_type',)
    list_filter = ('file_type',)

admin.site.register(CustomUrl, CustomUrlAdmin)