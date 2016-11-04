from django.apps import AppConfig


class ResizersConfig(AppConfig):
    name = 'resizers'

    def ready(self):
        import resizers.signals
