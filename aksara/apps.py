from django.apps import AppConfig


class AksaraConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aksara'
    INSTALLED_APPS = [
    'aksara.apps.AksaraConfig'
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
]
