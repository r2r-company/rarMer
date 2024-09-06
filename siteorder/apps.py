from django.apps import AppConfig

class SiteorderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'siteorder'

    def ready(self):
        import siteorder.signals  # Імпортуємо сигнали при готовності додатку
