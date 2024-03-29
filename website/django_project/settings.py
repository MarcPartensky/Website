"""
Django settings for django_project project.
Generated by 'django-admin startproject' using Django 2.1.
For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import sys
from urllib.parse import urlparse

# import dj_database_url
import mimetypes
import dotenv

mimetypes.add_type("text/css", ".css", True)

dotenv.load_dotenv()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG_VALUE") == "True"
# DEBUG = False
# TEMPLATE_DEBUG = DEBUG
# TEMPLATE_DEBUG = False

# if not DEBUG:
SESSION_COOKIE_SECURE = os.environ.get("SESSION_COOKIE_SECURE") or False
if os.environ.get("SECURE_PROXY_SSL_HEADER"):
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = os.environ.get("SECURE_SSL_REDIRECT") or False
SESSION_COOKIE_SECURE = os.environ.get("SESSION_COOKIE_SECURE") or False

ON_HEROKU = os.environ.get("ON_HEROKU")
HEROKU_SERVER = os.environ.get("HEROKU_SERVER")

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
SECRET_KEY = os.environ.get("SECRET_KEY")
# print('secret key:', SECRET_KEY)

ALLOWED_HOSTS = [
    "localhost",
    "marcpartensky.com",
    # "http://marcpartensky.com",
    # "https://marcpartensky.com",
]

CSRF_TRUSTED_ORIGINS = [
    "http://marcpartensky.com",
    "https://marcpartensky.com",
]

# Application definition

INSTALLED_APPS = [
    "url.apps.UrlConfig",
    "game.apps.GameConfig",
    "touch_typing.apps.TouchTypingConfig",
    "project.apps.ProjectConfig",
    "home.apps.HomeConfig",
    "planning.apps.PlanningConfig",
    "demo.apps.DemoConfig",
    "blog.apps.BlogConfig",
    "users.apps.UsersConfig",
    "first_site.apps.FirstSiteConfig",
    "test.apps.TestConfig",
    "chat.apps.ChatConfig",
    "isep.apps.IsepConfig",
    "gallery.apps.GalleryConfig",
    "design.apps.DesignConfig",
    "cdn.apps.CdnConfig",
    "api.apps.ApiConfig",
    "article.apps.ArticleConfig",
    "editor.apps.EditorConfig",
    "todo.apps.TodoConfig",
    "business.apps.BusinessConfig",
    "file.apps.FileConfig",
    "shell.apps.ShellConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "storages",
    "crispy_forms",
    "crispy_bootstrap4",
    "django_extensions",
    # allauth stuff
    "django.contrib.sites",
    "social_app",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # 'allauth.socialaccount.providers.google',
    # cors stuff
    # "corsheaders",
    # 503 error: maintenance service unavailable
    # 'django_503',
    # Compressor for scss to css
    "compressor",
    # Preview Markdown
    "markdown_view",
    "mdeditor",
    # Messing with sockets and channels for chat
    "channels",
    # Use ftp in production
    "django_ftpserver",
    # Read sql data
    "explorer",
    # Cluster manager
    "django_q",
    # Default avatar generator
    # "avatar",
    # Generate robots.txt
    "robots",
]

MIDDLEWARE = [
    "allauth.account.middleware.AccountMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # cors stuff
    "corsheaders.middleware.CorsMiddleware",
    # serve static files in production
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # 'django.middleware.common.CommonMiddleware',
    # 503 error
    # 'django_503.middleware.MaintenanceMiddleware',
]

# MIDDLEWARE = [] # for testing

CORS_ALLOW_HEADERS = (
    "x-requested-with",
    "content-type",
    "accept",
    "origin",
    "authorization",
    "x-csrftoken",
    "x-frame-options",
)

ROOT_URLCONF = "django_project.urls"

# Not safe
X_FRAME_OPTIONS = "SAMEORIGIN"

# https://stackoverflow.com/questions/29492617/base-template-for-all-apps-in-django
# print(os.path.join("django_project", 'templates'))
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            (os.path.join(BASE_DIR, "templates")),
        ],
        # "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "loaders": [
                (
                    "django.template.loaders.cached.Loader",
                    [
                        "django.template.loaders.filesystem.Loader",
                        "django.template.loaders.app_directories.Loader",
                    ],
                ),
            ],
        },
    },
    # {
    #     "BACKEND": "django.template.backends.django.DjangoTemplates",
    #     "APP_DIRS": True,
    # },
]

COMPRESS_PRECOMPILERS = (("text/x-scss", "django_libsass.SassCompiler"),)

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

WSGI_APPLICATION = "django_project.wsgi.application"

# Database
DATABASES = {}

postgres_name = os.environ.get("POSTGRES_DB")
if postgres_name:
    postgres_database = {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": postgres_name,
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    }
    DATABASES["default"] = postgres_database
    print("PostgreSQL logins detected, using those as default")

mysql_name = os.environ.get("MYSQL_DATABASE")
if mysql_name:
    mysql_database = {
        "ENGINE": "django.db.backends.mysql",
        "NAME": mysql_name,
        "USER": os.environ.get("MYSQL_USER"),
        "PASSWORD": os.environ.get("MYSQL_PASSWORD"),
        "HOST": os.environ.get("MYSQL_HOST"),
        "PORT": os.environ.get("MYSQL_PORT"),
    }
    if "default" not in DATABASES:
        DATABASES["default"] = mysql_database
        print("MySQL logins detected, using those as default")
    else:
        DATABASES["mysql"] = mysql_database
        print("MySQL logins detected, using as second database")

local_db = {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
}

if "default" not in DATABASES:
    DATABASES["default"] = local_db
    print("No database detected, using local MySQL database as default")
else:
    DATABASES["debug"] = local_db
    print("Using local MySQL database as debug database")


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
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"

LOGIN_REDIRECT_URL = "profile"
LOGIN_URL = "login"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASS")

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = "eu-west-3"

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

# if DEBUG:
# DEFAULT_FILE_STORAGE = MEDIA_ROOT
# else:
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# TEMPLATE_DIRS = (
#     os.path.join(os.path.dirname(__file__),'templates'),
# )

# allauth
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
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    }
}
# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ['GOOGLE_OAUTH2_KEY']
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ['GOOGLE_OAUTH2_SECRET']


REDIS_URL = (
    os.environ.get("REDIS_URL_STUNNEL")
    or os.environ.get("REDIS_URL")
    or os.environ.get("REDIS_TLS_URL")
    or "127.0.0.1:6379"
)

parse_result = urlparse(REDIS_URL)
REDIS_PORT = parse_result.port
REDIS_HOST = parse_result.hostname

# if ":" in REDIS_URL:
#     REDIS_HOST, REDIS_PORT = REDIS_URL.split(":")
#     REDIS_PORT = int(REDIS_PORT)
# else:
#     REDIS_HOST = REDIS_URL
#     REDIS_PORT = 6379

# print("Redis:", f"{REDIS_HOST}:{REDIS_PORT}")
# channel_hosts = [(REDIS_HOST, REDIS_PORT)]

channel_hosts = [REDIS_URL]

# Channels
ASGI_APPLICATION = "django_project.asgi.application"
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": channel_hosts,
            "symmetric_encryption_keys": [SECRET_KEY],
        },
        # "ROOTING": "chat.routing.channel_routing",
    },
}

REST_FRAMEWORK = {
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
    ]
}

MDEDITOR_CONFIGS = {
    "default": {
        "width": "100% ",  # Custom edit box width
        "heigth": "100%",  # Custom edit box height
        "toolbar": [
            "undo",
            "redo",
            "|",
            "bold",
            "del",
            "italic",
            "quote",
            "ucwords",
            "uppercase",
            "lowercase",
            "|",
            "h1",
            "h2",
            "h3",
            "h5",
            "h6",
            "|",
            "list-ul",
            "list-ol",
            "hr",
            "|",
            "link",
            "reference-link",
            "image",
            "code",
            "preformatted-text",
            "code-block",
            "table",
            "datetime",
            "emoji",
            "html-entities",
            "pagebreak",
            "goto-line",
            "|",
            "help",
            "info",
            "||",
            "preview",
            "watch",
            "fullscreen",
        ],  # custom edit box toolbar
        "upload_image_formats": [
            "jpg",
            "jpeg",
            "gif",
            "png",
            "bmp",
            "webp",
        ],  # image upload format type
        "image_folder": "editor",  # image save the folder name
        "theme": "default",  # edit box theme, dark / default
        "preview_theme": "default",  # Preview area theme, dark / default
        "editor_theme": "default",  # edit area theme, pastel-on-dark / default
        "toolbar_autofixed": True,  # Whether the toolbar capitals
        "search_replace": True,  # Whether to open the search for replacement
        "emoji": True,  # whether to open the expression function
        "tex": True,  # whether to open the tex chart function
        "flow_chart": True,  # whether to open the flow chart function
        "sequence": True,  # Whether to open the sequence diagram function
        "watch": True,  # Live preview
        "lineWrapping": False,  # lineWrapping
        "lineNumbers": False,  # lineNumbers
        "language": "fr",  # zh / en / es
    }
}

# SQL Explorer : https://pypi.org/project/django-sql-explorer/
# EXPLORER_DEFAULT_CONNECTION = 'readonly'

EXPLORER_CONNECTIONS = {"Default": "default"}
if "mysql" in DATABASES:
    EXPLORER_CONNECTIONS["Mysql"] = "mysql"
if "debug" in DATABASES:
    EXPLORER_CONNECTIONS["Debug"] = "debug"

EXPLORER_DEFAULT_CONNECTION = "default"

# settings.py example
Q_CLUSTER = {
    "name": "django_project",
    "workers": 8,
    "recycle": 500,
    "timeout": 60,
    "compress": True,
    "save_limit": 250,
    "queue_limit": 500,
    "cpu_affinity": 1,
    "label": "Django Q",
    "redis": {
        "host": REDIS_HOST,
        "port": REDIS_PORT,
        "db": 0,
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SILENCED_SYSTEM_CHECKS = ["urls.W002"]

PANDOC_API_URL = os.environ.get("PANDOC_API_URL") or "https://pandoc.marcpartensky.com"
