"""
Django settings for ShopMall project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9qsg0o^8ilhqm9o2$*=db=hdt=9dcs!*od0ejizi0o5_ubvknj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  #bug显示不显示给页面

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'xadmin',
    'crispy_forms',
    'reversion',
    'home',
    'goods',
    'DjangoUeditor',
]
#中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ShopMall.urls'



#模板路径
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],  #自定义模板目录
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',      #注册模板
                'public_return.public_car.public_car',
            ],
        },
    },
]


WSGI_APPLICATION = 'ShopMall.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
#数据库连接---读写分离
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shopmall',
        'USER':'root',
        'PASSWORD':'',
        'HOST':'127.0.0.1',
        'PORT':'3307',
        'OPTIONS': {
            # 'init_command': "SET foreign_key_checks=0;",
        }
    },
    'read': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shopmall',
        'USER':'root',
        'PASSWORD':'',
        'HOST':'127.0.0.1',
        'PORT':'3308',
        'OPTIONS':{
            # 'init_command':"SET foreign_key_checks=0;",
        }
    },

 }

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
# 认证
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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True  #字符串是否翻译翻译

USE_L10N = True  #给定语言环境格式

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
#静态文件上传和路径
STATIC_URL = '/static/'

STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static'),
    os.path.join(BASE_DIR,'static/ztree'),
]

#上传路径
MEDIA_URL='/media/'

MEDIA_ROOT=os.path.join(BASE_DIR,'media').replace('\\','/')

# 读写分离
DATABASE_ROUTERS=['ShopMall.router.Router',]