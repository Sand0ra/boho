from decouple import config

STATIC_URL = '/back_static/'
STATIC_ROOT = '/usr/src/app/back_static/'

MEDIA_URL = '/back_media/'
MEDIA_ROOT = '/usr/src/app/back_media/'

DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql',
        "NAME": config("POSTGRES_DB"),
        "USER": config("POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASSWORD"),
        "HOST": config("POSTGRES_HOST"),
        "PORT": config("POSTGRES_PORT"),
    }
}

CORS_ALLOW_HEADERS = [
    "accept",
    "Accept-Encoding",
    "authorization",
    "content-type",
    "Accept-Language",
    "Accept-Location",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]
CORS_ALLOW_ALL_ORIGINS = True

CSRF_TRUSTED_ORIGINS = ["http://34.71.213.250", "http://34.71.213.250:80", 'https://urfa-med.pp.ua']
