from pkg_resources import get_distribution

import django

if django.VERSION < (3, 2):
    default_app_config = "axes.apps.AppConfig"

__version__ = "5.27.0.1"
