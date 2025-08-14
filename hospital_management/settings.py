import os
import dj_database_url
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, '.env'))

     # Security settings
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-secret-key')
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
ALLOWED_HOSTS = ['*']  # Temporary; update to your Render domain after deployment

     # Application definition
INSTALLED_APPS = [
         'django.contrib.admin',
         'django.contrib.auth',
         'django.contrib.contenttypes',
         'django.contrib.sessions',
         'django.contrib.messages',
         'django.contrib.staticfiles',
         'hospital',
     ]

MIDDLEWARE = [
         'django.middleware.security.SecurityMiddleware',
         'whitenoise.middleware.WhiteNoiseMiddleware',
         'django.contrib.sessions.middleware.SessionMiddleware',
         'django.middleware.common.CommonMiddleware',
         'django.middleware.csrf.CsrfViewMiddleware',
         'django.contrib.auth.middleware.AuthenticationMiddleware',
         'django.contrib.messages.middleware.MessageMiddleware',
         'django.middleware.clickjacking.XFrameOptionsMiddleware',
     ]

ROOT_URLCONF = 'hospital_management.urls'
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

WSGI_APPLICATION = 'hospital_management.wsgi.application'

     # Database
DATABASES = {
         'default': dj_database_url.parse(
             os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')),
             conn_max_age=600
         )
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

     # Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

     # Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'