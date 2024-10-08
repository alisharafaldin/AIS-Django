import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5a&qb+fj^5eh_3p9q1$bpsu0@lz=^&p+d8#3-5ci_zv^#h6tim'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '192.168.1.4', '192.168.226.208', '192.168.0.105', '192.168.0.123', '192.168.0.107']

# Application definition

INSTALLED_APPS = [
    'basicinfo.apps.BasicinfoConfig',
    'employees.apps.EmployeesConfig',
    'companys.apps.CompanysConfig',
    'products.apps.ProductsConfig',
    'orders.apps.OrdersConfig',
    'pages.apps.PagesConfig',
    'profiles.apps.ProfilesConfig',
    'accounts.apps.AccountsConfig',
    'inventorys.apps.InventorysConfig',
    'dalilalaemal.apps.DalilalaemalConfig',
    'sales.apps.SalesConfig',
    'cashreceipt.apps.CashreceiptConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',
    'django.contrib.humanize',
    'purchases.apps.PurchasesConfig',
    'taggit',
    'rest_framework',
    'corsheaders',
    'django_select2',
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
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # عنوان React app
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
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation

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

LANGUAGES = [
    ('ar', _('Arabic')),
    ('en', _('English')),
]
LANGUAGE_CODE = 'ar'  # تعيين اللغة الافتراضية إلى العربية

TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_ROOT =  os.path.join(BASE_DIR , 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR , 'AIS/static')]

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

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'webmaster@localhost'