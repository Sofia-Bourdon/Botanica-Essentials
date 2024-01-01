 from django.apps import AppConfig  # noqa


class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        import checkout.signals   # noqa
