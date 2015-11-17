import os

from django.conf import global_settings

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.mysql',

        'HOST': 'localhost',

        #'USER': 'students_db_user',

        #'PASSWORD': 'password',

        'USER': 'root',

        'PASSWORD': '222',

        'NAME': 'students-db',

        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci',
        }


    }

 }