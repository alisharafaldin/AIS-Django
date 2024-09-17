from django.apps import AppConfig

class BasicinfoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basicinfo'

    def ready(self):
        import basicinfo.signals

    