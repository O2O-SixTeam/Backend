"""
Django settings for Cardoc project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import json

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('MODE') == 'DEBUG'
DB_RDS = os.environ.get('DB') == 'RDS'
DEBUG = True
DB_RDS = True

print('DEBUG : {}'.format(DEBUG))
print('DB_RDS: {}'.format(DB_RDS))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)
CONF_DIR = os.path.join(ROOT_DIR, '.conf-secret')

# Templates path
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(ROOT_DIR, 'static_root')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    STATIC_DIR,
)

# CONFIG FILE
CONFIG_FILE_COMMON = os.path.join(CONF_DIR, 'settings_common.json')
CONFIG_FILE = os.path.join(CONF_DIR, 'settings_local.json' if DEBUG else 'settings_deploy.json')
print('CONFIG_FILE : {}'.format(CONFIG_FILE))

config_common = json.loads(open(CONFIG_FILE_COMMON).read())
config = json.loads(open(CONFIG_FILE).read())

for key, key_dict in config_common.items():
    if not config.get(key):
        config[key] = {}
    for inner_key, inner_key_dict in key_dict.items():
        config[key][inner_key] = inner_key_dict

print(config)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config['django']['secret_key']
ALLOWED_HOSTS = config['django']['allowed_hosts']

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    )
}
AUTH_USER_MODEL = 'User.CustomUser'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'User',
    'Shop',
    'Request',
    'Estimate',
    'rest_auth',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'django_filters',

]
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_WHITELIST = (
    'kardoc.kr:8000',
    'localhost:8000',
    'ec2-13-124-46-207.ap-northeast-2.compute.amazonaws.com:8000'
)
ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATE_DIR,
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

## AWS RDS U: taehn / P: 1234qwer

if DEBUG and DB_RDS:
    # DEBUG 모드이며 DB_RDS옵션일 경우 로컬 postgreSQL이 아닌 RDS로 접속해 테스트한다
    config_db = config['db_rds']
else:
    # 그 외의 경우에는 해당 db설정을 따름
    config_db = config['db']

DATABASES = {
    'default': {
        'ENGINE': config_db['engine'],
        'NAME': config_db['name'],
        'USER': config_db['user'],
        'PASSWORD': config_db['password'],
        'HOST': config_db['host'],
        'PORT': config_db['port'],
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ko-KR'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True
