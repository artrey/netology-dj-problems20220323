from django.apps import AppConfig


class DemoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'demo'

    def ready(self):
        print('hello from config')
