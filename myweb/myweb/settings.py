"""
Django settings for myweb project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/
ADMINS = (((os.getenv('ADMIN_NAME', 'tester')), os.getenv('ADMIN_EMAIL', 'tester@tester.cc')),)
MANAGERS = ADMINS

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4jbpe0ie@0q+0#63nqap_xhc$2f&s!+zb($ytg@+ljs_a_-)s_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [os.getenv('ALLOWED_HOSTS', '*'), ]

SITE_ID = os.getenv('SITE_ID', int(2))

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'django.contrib.sites',

	'home',
	'blog',
	'foto',
	'about',
	# 'config',

	'theme',
	'labels',

	'sekizai',
	'compressor',
	'django_extensions',
	"ckeditor",
	"ckeditor_uploader",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

)

ROOT_URLCONF = 'myweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
				'django.core.context_processors.i18n',
                'django.contrib.messages.context_processors.messages',

				'myweb.context_processors.current_site',
				'sekizai.context_processors.sekizai',
            ],
        },
    },
]

WSGI_APPLICATION = 'myweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'ymedb',
	 'USER': 'ymeroot',
         'PASSWORD': 'y2017829yq',
         'host': '127.0.0.1',
          }
	# 'default': dj_database_url.config(default= 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'))
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LOCALE_PATHS = (
	os.path.join(BASE_DIR, 'locale'),
)

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	'compressor.finders.CompressorFinder',
)

STATIC_URL = '/static/'
STATIC_ROOT = os.getenv('STATIC_ROOT', os.path.join(BASE_DIR, 'static'))
MEDIA_URL = '/media/'
MEDIA_ROOT = os.getenv('MEDIA_ROOT', os.path.join(BASE_DIR, 'media'))
CKEDITOR_UPLOAD_PATH = 'upload/'

# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': 'full',
#         'height': 300,
#         'width': "80%",
#     },
# }
