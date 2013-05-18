# coding: utf-8

from ._base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'children',
        'USER': 'children',
        'PASSWORD': 'children',
        'HOST': 'localhost',
        'PORT': '',
    }
}
