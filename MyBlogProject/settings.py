"""
Django settings for MyBlogProject project.

Generated by 'django-admin startproject' using Django 1.11.6.

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
SECRET_KEY = 'v&o^+w2v6gjojhnyxhcp*wu6+d3t^0tx#mz_zj&fm3ks@d)yk*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# *表示允许所有域名，并不推荐这么干。
ALLOWED_HOSTS = ['*',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haystack',
    'blogauth',
    'blog',
    'comments',
    'markdownx',
    'gunicorn',
]

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'blog.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}


HAYSTACK_SEARCH_RESULTS_PER_PAGE = 5
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MyBlogProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join (BASE_DIR, 'templates')]
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

WSGI_APPLICATION = 'MyBlogProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# 因为使用markdown，支持上传图片的功能，所以必须设置MEDIA_ROOT

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(__file__),'media')

#
# MARKDOWNX_MARKDOWN_EXTENSIONS = []
# MARKDOWNX_MEDIA_PATH = 'markdownx/' # subdirectory, where images will be stored in MEDIA_ROOT folder
# MARKDOWNX_UPLOAD_MAX_SIZE = 52428800 # 50MB
# MARKDOWNX_UPLOAD_CONTENT_TYPES = ['image/jpeg', 'image/png']
# MARKDOWNX_IMAGE_MAX_SIZE = {'size': (500, 500), 'quality': 90,}
# MARKDOWNX_EDITOR_RESIZABLE = True # update editor's height to inner content height while typing


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'


# 当运行 python manage.py collectstatic 的时候
# STATIC_ROOT 文件夹 是用来将所有STATICFILES_DIRS中所有文件夹中的文件，以及各app中static中的文件都复制过来
# 把这些文件放到一起是为了用apache等部署的时候更方便


STATIC_ROOT = os.path.join (BASE_DIR, 'collected_static')

# 其它 存放静态文件的文件夹，可以用来存放项目中公用的静态文件，里面不能包含 STATIC_ROOT
# 如果不想用 STATICFILES_DIRS 可以不用，都放在 app 里的 static 中也可以

STATICFILES_DIRS = (
    os.path.join (BASE_DIR, "common_static"),
    # '/path/to/others/static/',  # 用不到的时候可以不写这一行
)

# 这个是默认设置，Django 默认会在 STATICFILES_DIRS中的文件夹 和 各app下的static文件夹中找文件
# 注意有先后顺序，找到了就不再继续找了
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
)




AUTH_USER_MODEL = 'blogauth.User'

LOGIN_URL = '/login'


LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'blogauth.backends.EmailBackend',
)

# 用于开发测试邮件发送的settings设置选项。
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# 以下安全选项涉及的默认值均为False，

# 默认值为0，一般生产上设为31536000秒，一年，意思是告诉浏览器，看到https协议头，就要在这段时间内拒绝http访问你的域名。
SECURE_HSTS_SECONDS = 60

# 将HTTP链接永久地（HTTP 301，permanently）重定向到HTTPS连接。一般别开启该选项，会造成http直接跳转到https的，还得清理浏览器缓存才能恢复。
SECURE_SSL_REDIRECT = False

#如果True，则SecurityMiddleware在尚未拥有它的所有响应上设置X-Content-Type-Options: nosniff，
# nosniff选项意味着防止浏览器猜测内容类型，并强制它始终使用Content-Type标题中提供的类型，
SECURE_CONTENT_TYPE_NOSNIFF = True

# 如果True，SecurityMiddleware设置X-XSS-Protection: 1; mode=block,这将在浏览器中启用XSS筛选器，并强制它始终阻止可疑的XSS攻击。
# 这是个有效手段，但是不能保证检测到所有的XSS攻击，也不是所有浏览器都支持。
SECURE_BROWSER_XSS_FILTER = True

# 如果True，SecurityMiddleware将preload指令添加到HTTP Strict Transport Security头。 参考资料https://developer.mozilla.org/zh-CN/docs/Web/HTML/Preloading_content；
# 仅仅当SECURE_HSTS_SECONDS设置为非零值，它才起作用。
SECURE_HSTS_PRELOAD = True

# 如果True，则SecurityMiddleware将includeSubDomains指令添加到HTTP Strict Transport Security头。
# 仅仅当SECURE_HSTS_SECONDS设置为非零值，它才起作用。
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# 默认值：False，如果此设置为True，则Cookie将被标记为“安全”，这意味着浏览器可以确保该Cookie仅在HTTPS连接下发送。
SESSION_COOKIE_SECURE = False

# 默认值：False，如果将此设置为True，则Cookie将被标记为“安全”，这意味着浏览器可能会确保Cookie仅使用HTTPS连接发送。
CSRF_COOKIE_SECURE = False

X_FRAME_OPTIONS  = 'DENY'