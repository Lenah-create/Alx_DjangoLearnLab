"""
Django settings for LibraryProject project.
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-12bu+#8)lu$rvwut#%-_gp%8nnd)6rfw9#a3=hvd@c9g($cl1y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Browser security headers
SECURE_BROWSER_XSS_FILTER = True         # Enables XSS protection in modern browsers
SECURE_CONTENT_TYPE_NOSNIFF = True       # Prevents the browser from guessing content types
X_FRAME_OPTIONS = 'DENY'                 # Protects against clickjacking

# Cookie security
CSRF_COOKIE_SECURE = True                # CSRF cookies only sent via HTTPS
SESSION_COOKIE_SECURE = True             # Session cookies only sent via HTTPS
CSRF_COOKIE_HTTPONLY = True              # Prevents JS access to CSRF cookie
SESSION_COOKIE_HTTPONLY = True           # Prevents JS access to session cookie


# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000          # One year in seconds
SECURE_HSTS_INCLUDE_SUBDOMAINS = True   # Include subdomains in HSTS policy
SECURE_HSTS_PRELOAD = True              # Allow site to be preloaded by browsers

# Secure headers for reverse proxy / load balancer
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Optional: Force HTTPS
SECURE_SSL_REDIRECT = True               # Redirect HTTP -> HTTPS


CSP_DEFAULT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")
CSP_SCRIPT_SRC = ("'self'",)

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # your apps
    'users',             # custom user model app
    'bookshelf',         # bookshelf app
    'relationship_app',  # relationship app

    'csp',

    'sslserver',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
    'LibraryProject.middleware.ContentSecurityPolicyMiddleware',
]

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LibraryProject.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Use custom user model
AUTH_USER_MODEL = 'users.CustomUser'

AUTH_USER_MODEL = "bookshelf.CustomUser"

# Optional: media files for profile photos
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
