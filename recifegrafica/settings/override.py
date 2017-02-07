# encoding: utf-8


from base import *
USE_LESS = False
LESSC_BIN = os.path.join(BASE_DIR, 'node_modules', '.bin', 'lessc')
COMPRESS_PRECOMPILERS = (
    ('text/less', '%s {infile}'%LESSC_BIN),
)
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]

#CIELO CONFIGURACOES

##TESTES
# OSCAR_CIELO_NUMERO="1006993069"
# OSCAR_CIELO_CHAVE="25fbb99741c739dd84d7b06ec78c9bac718838630f30b112d033ce2e621b34f3"
# OSCAR_CIELO_SANDBOX= True

##NOSSOS NUMEROS
OSCAR_CIELO_NUMERO="1088067821"
OSCAR_CIELO_CHAVE="efb6cfe18f054db04c37083935b40281609d6c564b8c00b5cae3cc595007c7e5"
OSCAR_CIELO_SANDBOX= False


#Não cadastrados podem comprar
OSCAR_ALLOW_ANON_CHECKOUT = False

#LOGGER

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s',
        },
        'simple': {
            'format': '[%(asctime)s] %(message)s'
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console'],
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'oscar': {
            'level': 'DEBUG',
            'propagate': True,
        },
        'oscar.catalogue.import': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'oscar.alerts': {
            'handlers': ['null'],
            'level': 'INFO',
            'propagate': False,
        },

        # Django loggers
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'level': 'WARNING',
            'propagate': True,
        },
        # Third party
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sorl.thumbnail': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
    }
}

## PHONES ##

PHONENUMBER_DEFAULT_REGION = 'BR'

# EMAIL CONFIGURATION #

OSCAR_FROM_EMAIL = 'admin@3ecologias.net'
DEFAULT_FROM_EMAIL = 'admin@3ecologias.net'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'juliaroberts@3ecologias.net'
EMAIL_HOST_PASSWORD = 'Tatub0lana0b0la'
EMAIL_USE_TLS = True
EMAIL_PORT = 587

#############################
##~DASHBOARD CONFIGURATION~##
#############################

OSCAR_DASHBOARD_NAVIGATION.append({
    'label': 'Frete',
    'icon': 'icon-truck',
    'url_name': 'dashboard:shipping-method-list'
})

# OSCAR_DASHBOARD_NAVIGATION.append({
#     'label': 'Artes',
#     'icon': 'icon-truck',
#     'url_name': 'arts-list'
# })
