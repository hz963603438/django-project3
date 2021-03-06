"""
Django settings for django_project3 project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-&b)_+89%vuw22s*)768@v)tm#p2i+3k_vbex!@#z)k46*i9+n'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = False
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'monitor.apps.MonitorConfig',
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

ROOT_URLCONF = 'django_project3.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'django_project3.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django-db1',
        'USER': 'root',                                 # ?????????
        'PASSWORD': '9povNOGFF6GX45s5BrD1',             # ??????
        'HOST': 'test-gerp-search-29.cchl8ctvt28p.rds.cn-northwest-1.amazonaws.com.cn',       # ??????
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

#???????????????url???????????????????????????????????????,????????????WEB????????????URL??????
STATIC_URL = '/static/'

# ????????????????????????????????????????????????????????????STATIC_ROOT?????????STATIC_ROOT ??? STATICFILES_DIRS?????????????????????
#STATICFILES_DIRS = [
    #os.path.join(BASE_DIR, 'monitor', 'static')
    #os.path.join(BASE_DIR,  'static')
#]


#the dir for command "python manage.py collectstatic"
# ??????collectstatic????????????????????????????????????????????????STATICFILES_DIRS?????????admin??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
STATIC_ROOT = os.path.join(BASE_DIR, "static")

SIMPLEUI_HOME_ACTION = True

SIMPLEUI_HOME_QUICK = True

#SIMPLEUI_HOME_PAGE = 'http://161.189.80.188:8066'

#SIMPLEUI_HOME_TITLE = '????????????????????????'

SIMPLEUI_HOME_ICON = 'fa fa-user'

SIMPLEUI_INDEX = 'https://www.88cto.com'

#SIMPLEUI_LOGO = 'https://avatars2.githubusercontent.com/u/13655483?s=60&v=4'

#system_keep = True

#menu_display = True

#dynamic = True

SIMPLEUI_DEFAULT_ICON = True

