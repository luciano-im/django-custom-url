from django.apps import AppConfig


class CustomUrlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_url'
    verbose_name = 'Custom URL'
