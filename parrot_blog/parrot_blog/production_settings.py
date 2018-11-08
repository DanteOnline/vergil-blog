DEBUG = False

DATABASES = {
    'default': {
        'NAME': 'wavymain',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'admin',
        'PASSWORD': '1',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}