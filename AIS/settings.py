"""
Django settings for AIS project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5a&qb+fj^5eh_3p9q1$bpsu0@lz=^&p+d8#3-5ci_zv^#h6tim'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '192.168.1.6']


# Application definition

INSTALLED_APPS = [
    'shrfntod.apps.ShrfntodConfig',
    'basicinfo.apps.BasicinfoConfig',
    'hadena.apps.HadenaConfig',
    'employees.apps.EmployeesConfig',
    'companys.apps.CompanysConfig',
    'products.apps.ProductsConfig',
    'orders.apps.OrdersConfig',
    'pages.apps.PagesConfig',
    'profiles.apps.ProfilesConfig',
    'accounts.apps.AccountsConfig',
    'forex.apps.ForexConfig',
    'effastore.apps.EffastoreConfig',
    'dalilalaemal.apps.DalilalaemalConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',
    'django.contrib.humanize',
    'taggit',
    'rest_framework',
    'purchases.apps.PurchasesConfig',
    'sales.apps.SalesConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'companys.middleware.CurrentCompanyMiddleware',
]

ROOT_URLCONF = 'AIS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join( BASE_DIR , 'templates')],
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

WSGI_APPLICATION = 'AIS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': 'timesheetdb',
        # 'USER' : 'postgres',
        # 'PASSWORD' : '2468',
        # 'HOST' : 'localhost',
        # 'PORT' : '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGES = [
    ('ar', _('Arabic')),
    ('en', _('English')),
]
LANGUAGE_CODE = 'ar'  # تعيين اللغة الافتراضية إلى العربية

# LOCALE_PATHS = [
#     os.path.join(BASE_DIR, 'locale'),  # مجلد الترجمة
# ]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_ROOT =  os.path.join(BASE_DIR , 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
     os.path.join(BASE_DIR , 'AIS/static')
]

#Msdia Folder
MEDIA_ROOT =  os.path.join(BASE_DIR , 'media')
MEDIA_URL = '/media/'

LOGIN_URL = '/profiles/signin'


#Custom Messages
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}
# f = open('test.txt', 'w')
# f.write( os.path.join(BASE_DIR))
# f.close()

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# إعدادات البريد الإلكتروني لإستعادة كلمة المرور
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.your-email-provider.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'alisharafaldin@gmail.com'
# EMAIL_HOST_PASSWORD = 'kd]ghthvadgu@GA01'
# DEFAULT_FROM_EMAIL = 'info@ais.com'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'webmaster@localhost'
