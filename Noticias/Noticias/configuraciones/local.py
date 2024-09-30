from .settings import *

DEBUG = True


ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


#EMAIL_BACKEND = 'django.core.mail.blackends.smtp.EmailBackend'
#EMAIL_HOST = 'smt.gmail.com'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'correo@gmail.com'
#EMAIL_USE_TLS = True
#DEFAULT_FROM_EMAIL = 'correo@gmail.com'