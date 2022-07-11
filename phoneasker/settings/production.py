import os
from .base import *

DB_NAME = os.environ['DB_NAME']
DB_USER = os.environ['DB_USER']
DB_PASS = os.environ['DB_PASS']

ALLOWED_HOSTS = [
    'bots.stroy-kran.ru',
    'www.bots.stroy-kran.ru',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
