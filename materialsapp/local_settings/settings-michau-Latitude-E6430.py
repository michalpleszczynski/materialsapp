# coding: utf-8
DEBUG = True
TEMPLATE_DEBUG = DEBUG

DEBUG_SQL = False

if DEBUG_SQL:

    LOGGING['loggers'].update({
        # Only becomes active with DEBUG = True
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console_sql'],
            'propagate': False,
        },
    })