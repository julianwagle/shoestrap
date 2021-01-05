from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ExamplesConfig(AppConfig):
    name = "base.examples"
    verbose_name = _("Examples")


