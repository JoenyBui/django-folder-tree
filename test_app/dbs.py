import os

from .settings import BASE_DIR, DEBUG

DB = "postgresql"

__author__ = 'jbui'

if DB == "postgresql":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'django-folder-tree',
            'USER': 'debug',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

elif DB == 'sqlite':

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }