
STATIC_URL = '/back-static/'
STATIC_ROOT = '/usr/src/app/back_static/'

MEDIA_URL = '/back-media/'
MEDIA_ROOT = '/usr/src/app/back_media/'

CSRF_TRUSTED_ORIGINS = ["http://localhost", "http://localhost:80"]

CORS_ALLOW_ALL_ORIGINS = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}
