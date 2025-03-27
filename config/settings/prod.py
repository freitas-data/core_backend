from .base import *

DEBUG = False
ALLOWED_HOSTS = ['*']  # Você pode depois trocar pelo domínio final do Railway

CSRF_TRUSTED_ORIGINS = ['https://*.railway.app']
