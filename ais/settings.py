from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# تحديد مسار المجلد static الموجود في جذر المشروع
STATIC_URL = '/static/'  # الرابط الذي سيستخدم للوصول إلى ملفات static
# تحديد مسار جمع ملفات static في الإنتاج
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# تحديد مسار البحث عن ملفات static داخل المجلدات في المشروع
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!jh7*^y0ypid3zm^*di7-)21)3e4wpbi+*@4*rb@#p1zsu-41f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.dalilalaemal.com','192.168.1.4']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'import_export',
    'django.contrib.humanize',
    'pages.apps.PagesConfig',
    'dalilalaemal.apps.DalilalaemalConfig',
    'basicinfo.apps.BasicinfoConfig',
    'companys.apps.CompanysConfig',
    'profiles.apps.ProfilesConfig',
    'employees.apps.EmployeesConfig',
    'products.apps.ProductsConfig',
    'inventorys.apps.InventorysConfig',
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
]

ROOT_URLCONF = 'ais.urls'

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

WSGI_APPLICATION = 'ais.wsgi.application'

# Database
from dotenv import load_dotenv #بمتطلبات متغيرات البيئة
load_dotenv()  # لتحميل المتغيرات من ملف .env
# استرجاع قيمة متغير البيئة
environment = os.getenv('ENV', 'development')  # 'development' هي القيمة الافتراضية

if environment == 'production':
    # إعدادات بيئة الإنتاج
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'alisharafaldinal$aisdb',
            'USER': 'alisharafaldinal',
            'PASSWORD': 'asa13579@MA01',
            'HOST': 'alisharafaldinali.mysql.pythonanywhere-services.com',
            'PORT': '3306',
        }
    }
    print("Running in Production Environment")
else:
    # إعدادات بيئة التطوير
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    print("Running in Development Environment")
    


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LOGIN_URL = '/profiles/signin/'  # استبدل '/custom-login/' بالمسار الخاص بك

# إعداد إستعادة كلمة المرور
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # مضيف SMTP الصحيح لـ Gmail
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'dalilalaemal@gmail.com'
EMAIL_HOST_PASSWORD = 'asa13579@GD01'  # كلمة المرور لحساب Gmail (أو كلمة مرور التطبيق إذا كنت تستخدم التحقق بخطوتين)
DEFAULT_FROM_EMAIL = 'dalilalaemal@gmail.com'
