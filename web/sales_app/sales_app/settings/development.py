from .base import *  # noqa

DEBUG = True

INTERNAL_IPS = ["172.18.0.5", "127.0.0.1", "0.0.0.0"]

SECRET_KEY = 'xw6zimru2&y8iqg$9fhi9#vm7gkd_xvrouc%1-k7l)w(qca#xg'

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# DJANGO DEBUG TOOLBAR SETTINGS
# https://django-debug-toolbar.readthedocs.org
def show_toolbar(request):
    """
     Show the debug toolbar
    """
    return not request.is_ajax() and request.user and request.user.is_superuser


MIDDLEWARE_CLASSES += ["debug_toolbar.middleware.DebugToolbarMiddleware", ]
INSTALLED_APPS += ["debug_toolbar", ]
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'HIDE_DJANGO_SQL': True,
    'TAG': 'body',
    'SHOW_TEMPLATE_CONTEXT': True,
    'ENABLE_STACKTRACES': False,
    'SHOW_TOOLBAR_CALLBACK': 'sales_app.settings.development.show_toolbar',
}

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
)

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        }
    },
}

try:
    from local_settings import * # noqa
except ImportError:
    pass
