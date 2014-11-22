from django.apps import AppConfig


class DefaultConfig(AppConfig):

    name = 'apps.bill'
    verbose_name = 'Bill'

    def ready(self):

        from . import listeners
