from django.apps import AppConfig


class ProfileConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Profile"
    verbose_name = "حساب کاربری"
    def ready(self):
        from . import signals
