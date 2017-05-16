import os
from django.contrib import messages

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'aj=^bfu%c34e08f&bh41v#kg9li_0rd-7uhzo(^b=9*wdv2bqf'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'mzitopowerltd.herokuapp.com', '0.0.0.0', 'localhost']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'mzito/templates'),
            os.path.join(BASE_DIR, 'mzito/templates'),
            os.path.join(BASE_DIR, 'mzito/templates'),
            os.path.join(BASE_DIR, 'mzito/templates'),
            os.path.join(BASE_DIR, 'mzito/templates'),
        ],
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

CRISPY_TEMPLATE_PACK = 'bootstrap3'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'deisaack@yahoo.com' #my gmail username
EMAIL_HOST_PASSWORD = 'YAHOO1' #my gmail password
EMAIL_PORT = 25 # 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "Isaac <deisaack@yahoo.com>"

ADMINS = (
  ('Prof. Isaac', 'deisaack@yahoo.com'),
)
# ADMINS = [('Isaac', EMAIL_HOST_USER)]
MANAGERS = ADMINS

INSTALLED_APPS = (
    'django.contrib.auth',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'authtools',
    "geoposition",
    'crispy_forms',
    'easy_thumbnails',

    'mzito.activities',
    'mzito.apply',
    'mzito.authentication',
    'mzito.core',
    'mzito.feeds',
    'mzito.messenger',
    'mzito.search',
    'mzito.operation',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
ROOT_URLCONF = 'mzito.urls'
WSGI_APPLICATION = 'mzito.wsgi.application'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_ROOT = os.path.join(BASE_DIR, 'live-static', 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'mzito/static'),
)
MEDIA_ROOT = os.path.join(BASE_DIR, 'live-static/media')
MEDIA_URL = '/media/'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/feeds/'
ALLOWED_SIGNUP_DOMAINS = ['*']
FILE_UPLOAD_TEMP_DIR = '/tmp/'
FILE_UPLOAD_PERMISSIONS = 0o644
THUMBNAIL_EXTENSION = 'png'
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}
GEOPOSITION_GOOGLE_MAPS_API_KEY = 'AIzaSyCKKERHiiwDU37DQ719Uj93bXVlSGRMn9U'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

