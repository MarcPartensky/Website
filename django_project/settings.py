"""
Django settings for django_project project.
Generated by 'django-admin startproject' using Django 2.1.
For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import django_heroku
# import dj_database_url

import dotenv

dotenv.load_dotenv()

SESSION_COOKIE_SECURE = True
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (os.environ.get('DEBUG_VALUE') == 'True')
# DEBUG = False
# TEMPLATE_DEBUG = DEBUG
# TEMPLATE_DEBUG = False

ON_HEROKU = os.environ.get('ON_HEROKU')
HEROKU_SERVER = os.environ.get('HEROKU_SERVER')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Allowing cors
CORS_ORIGIN_ALLOW_ALL = False
# CORS_ORIGIN_WHITELIST = (
    # 'google.com',
    # 'websiteofmarcpartensky.herokuapp.com'
# )

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'exhlfdat&vfum(-34*c2uroi(($ww(yo$9pv98=e6p^gl(-eoj'
SECRET_KEY = os.environ.get('SECRET_KEY')
# print('secret key:', SECRET_KEY)


ALLOWED_HOSTS = ["websiteofmarcpartensky.herokuapp.com", "localhost"]

# Application definition

INSTALLED_APPS = [
    'game.apps.GameConfig',
    'touch_typing.apps.TouchTypingConfig',
    'project.apps.ProjectConfig',
    'home.apps.HomeConfig',
    'planning.apps.PlanningConfig',
    'demo.apps.DemoConfig',
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    'first_site.apps.FirstSiteConfig',
    'test.apps.TestConfig',
    'chat.apps.ChatConfig',
    'isep.apps.IsepConfig',
    'gallery.apps.GalleryConfig',
    'design.apps.DesignConfig',
    'cdn.apps.CdnConfig',
    'api.apps.ApiConfig',
    'article.apps.ArticleConfig',
    'editor.apps.EditorConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'crispy_forms',

    # allauth stuff
    'django.contrib.sites',
    'social_app',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',

    # cors stuff
    'corsheaders',

    # 503 error: maintenance service unavailable
    # 'django_503',

    # Compressor for scss to css
    'compressor',

    # Preview Markdown
    'markdown_view',
    'mdeditor',

    # Messing with sockets and channels for chat
    'channels',

    # Use ftp in production
    'django_ftpserver',

    # Read sql data
    'explorer',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # cors stuff
    'corsheaders.middleware.CorsMiddleware',
    # 'django.middleware.common.CommonMiddleware',

    # 503 error
    # 'django_503.middleware.MaintenanceMiddleware',
]

# MIDDLEWARE = [] # for testing

CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken'
    'x-frame-options',
)

ROOT_URLCONF = 'django_project.urls'

# Not safe
X_FRAME_OPTIONS = 'SAMEORIGIN'

# https://stackoverflow.com/questions/29492617/base-template-for-all-apps-in-django
# print(os.path.join("django_project", 'templates'))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(os.path.join(BASE_DIR, 'templates')),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            # 'loaders': [
            #     ('django.template.loaders.cached.Loader', [
            #         'django.template.loaders.filesystem.Loader',
            #         'django.template.loaders.app_directories.Loader',
            #     ]),
            # ],
        },
    },
]

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

WSGI_APPLICATION = 'django_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
if ON_HEROKU:
    DATABASE_URL = 'postgresql:///postgresql'
else:
    DATABASE_URL = 'sqlite://' + os.path.join(BASE_DIR, 'db.sqlite3')

# print("DATABASE_URL:",DATABASE_URL)
# DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}

# print("BASE_DIR:", BASE_DIR)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'production': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT'),
    }
}

# print('production port:', os.environ.get('POSTGRES_PORT'))

# print("DATABASES:", DATABASES)

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'DatabaseName',
#         'USER': 'DatabaseUserName',
#         'PASSWORD': 'DatabaseUserpassword',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    # '/var/www/static/',
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'profile'
LOGIN_URL = 'login'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = 'eu-west-3'

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# TEMPLATE_DIRS = (
#     os.path.join(os.path.dirname(__file__),'templates'),
# )

#allauth
# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
 # 'allauth.account.auth_backends.AuthenticationBackend',
    # 'social_core.backends.open_id.OpenIdAuth',
    # 'social_core.backends.google.GoogleOpenId',
    # 'social_core.backends.google.GoogleOAuth2',
    # 'social_core.backends.google.GoogleOAuth',
    # 'social_core.backends.facebook.FacebookOAuth2',
# )
SITE_ID = 1
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}
# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ['GOOGLE_OAUTH2_KEY']
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ['GOOGLE_OAUTH2_SECRET']

REDIS_URL = os.environ.get('REDIS_URL_STUNNEL') or \
            os.environ.get('REDIS_URL') or \
            os.environ.get('REDIS_TLS_URL')


if DEBUG:
    debug_hosts = [('127.0.0.1', 6379)]
else:
    debug_hosts = []

# Channels
ASGI_APPLICATION = 'django_project.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": debug_hosts + [
                REDIS_URL,
                # 'redis://localhost:6379'
            ],
            "symmetric_encryption_keys": [SECRET_KEY],
        },
        "ROOTING": "chat.routing.channel_routing",
    },
}

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ]
}

MDEDITOR_CONFIGS = {
    'default':{
        'width': '100% ',  # Custom edit box width
        'heigth': '100%',  # Custom edit box height
        'toolbar': [
            "undo", "redo", "|",
            "bold", "del", "italic", "quote", "ucwords", "uppercase", "lowercase", "|",
            "h1", "h2", "h3", "h5", "h6", "|",
            "list-ul", "list-ol", "hr", "|",
            "link", "reference-link", "image", "code", "preformatted-text", "code-block", "table", "datetime",
            "emoji", "html-entities", "pagebreak", "goto-line", "|",
            "help", "info",
            "||", "preview", "watch", "fullscreen"
        ],  # custom edit box toolbar
        'upload_image_formats': ["jpg", "jpeg", "gif", "png", "bmp", "webp"],  # image upload format type
        'image_folder': 'editor',  # image save the folder name
        'theme': 'default',  # edit box theme, dark / default
        'preview_theme': 'default',  # Preview area theme, dark / default
        'editor_theme': 'default',  # edit area theme, pastel-on-dark / default
        'toolbar_autofixed': True,  # Whether the toolbar capitals
        'search_replace': True,  # Whether to open the search for replacement
        'emoji': True,  # whether to open the expression function
        'tex': True,  # whether to open the tex chart function
        'flow_chart': True,  # whether to open the flow chart function
        'sequence': True, # Whether to open the sequence diagram function
        'watch': True,  # Live preview
        'lineWrapping': False,  # lineWrapping
        'lineNumbers': False,  # lineNumbers
        'language': 'fr'  # zh / en / es
    }
}

# SQL Explorer : https://pypi.org/project/django-sql-explorer/
# EXPLORER_DEFAULT_CONNECTION = 'readonly'
EXPLORER_CONNECTIONS = {'Default': 'default', 'Production': 'production'}
# EXPLORER_CONNECTIONS = { 'Default': 'default' }
EXPLORER_DEFAULT_CONNECTION = 'production'


django_heroku.settings(locals())
