import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-mgcuwo=b7)%55h(72&mw3fs8(f^5562#uf!x$52kt9jj*w70_t'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'uznavaika',
        'USER': 'uznavaika_user',
        'PASSWORD': 'uznavaika',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# STATIC_URL = '/static/'
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]
