"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from django.utils.translation import gettext_lazy as _
from decouple import config
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

PRODUCTION = config("PRODUCTION", cast=bool)

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'modeltranslation',
    'corsheaders',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'apps.menu',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}


WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ('ru', _('Russian')),
    ('en', _('English')),
]

STATIC_URL = '/back_static/'
STATIC_ROOT = BASE_DIR / 'back_static'

MEDIA_URL = '/back_media/'
MEDIA_ROOT = BASE_DIR / 'back_media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


JAZZMIN_SETTINGS = {
    "site_title":
    "URFA",  # Заголовок админ-панели
    "site_header":
    "URFA",  # Заголовок на экране входа
    "site_brand":
    "Администрация сайта",  # Бренд в верхней части админ-панели
    "welcome_sign":
    "Добро пожаловать в URFA",  # Приветственное сообщение

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon":
    None,

    # "topmenu_links": [
    #     {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
    # ],
    "show_sidebar":
    True,
    "changeform_format":
    "horizontal_tabs",
    "header_classes":
    "navbar-dark bg-dark",  # Темный фон верхней части админ-панели
    "header_color":
    "#000000",  # Черный цвет верхней части админ-панели
    "dark_mode_theme":
    True,  # Включить темный режим
    "show_language_chooser":
    True,  # Включить выбор языка в админ-панели
    "custom_css":
    None,  # Путь к пользовательскому CSS-файлу (если нужен)
    "show_ui_builder":
    True,  # Показать UI Builder
    "icons": {
        "menu.Chart": "fas fa-regular fa-clock",
        "menu.Event": "fas fa-calendar-alt",
        "menu.MenuCategory": "fas fa-clipboard-list",
        "menu.MenuSubCategory": "fas fa-list-alt",
        "menu.MenuPosition": "fas fa-utensils"
    }
}

# Выбрал только то что мне понравилось если что можем поменять тему
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": True,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "cyborg",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": True
}

if DEBUG:
    INTERNAL_IPS = ["127.0.0.1"]
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": lambda request: True,
    }
    INSTALLED_APPS += [
        'debug_toolbar',
    ]


if PRODUCTION:
    from .prod import *
    INSTALLED_APPS += [
        'drf_spectacular',
    ]

    REST_FRAMEWORK['DEFAULT_SCHEMA_CLASS'] = 'drf_spectacular.openapi.AutoSchema'

    SPECTACULAR_SETTINGS = {
        'TITLE': 'BOHO-API',
        'DESCRIPTION': 'Это API нашего проекта BOHO beach bar',
        'VERSION': '1.0.0',
        'OPENAPI_VERSION': '3.0.0',
    }
else:
    from .locale import *
    INSTALLED_APPS += [
        'drf_spectacular',
    ]

    REST_FRAMEWORK['DEFAULT_SCHEMA_CLASS'] = 'drf_spectacular.openapi.AutoSchema'

    SPECTACULAR_SETTINGS = {
        'TITLE': 'BOHO-API',
        'DESCRIPTION': 'Это API нашего проекта BOHO beach bar',
        'VERSION': '1.0.0',
        'OPENAPI_VERSION': '3.0.0',
    }
