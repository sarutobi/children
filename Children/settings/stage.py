# -*- coding: utf-8 -*-

from ._base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'children',
        'USER': 'children',
        'PASSWORD': 'DevChildren',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_ROOT = os.path.join(get_env_var('STATIC_ROOT'), 'children', 'static')
