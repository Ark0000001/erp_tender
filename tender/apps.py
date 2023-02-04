from django.apps import AppConfig


class TenderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tender'
    verbose_name='Менеджер задач'
    def ready(self):
        from .scheduler import scheduler
        scheduler.start()
