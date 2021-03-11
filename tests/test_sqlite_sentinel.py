DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}

SECRET_KEY = 'django_tests_secret_key'
TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
ADMIN_MEDIA_PREFIX = '/static/admin/'
STATICFILES_DIRS = ()

MIDDLEWARE_CLASSES = []
DJANGO_REDIS_LOG_IGNORED_EXCEPTIONS = False
CACHES = {
    'default': {
        'BACKEND': 'django_redis_sentinel.cache.RedisSentinelCache',
        'LOCATION': [
            ('127.0.0.1', 26380),
            ('127.0.0.1', 26381),
            ('127.0.0.1', 26382),
        ],
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis_sentinel.client.SentinelClient',
            'SENTINEL_SERVICE_NAME': 'rmaster',
            'REDIS_CLIENT_KWARGS': {
                'db': 1,
                'decode_responses': True,
            },
        },
    },
    'doesnotexist': {
        'BACKEND': 'django_redis_sentinel.cache.RedisSentinelCache',
        'LOCATION': [
            ('127.0.0.1', 26380),
            ('127.0.0.1', 26381),
            ('127.0.0.1', 26382),
        ],
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis_sentinel.client.SentinelClient',
            'SENTINEL_SERVICE_NAME': 'rmaster',
            'REDIS_CLIENT_KWARGS': {
                'db': 1,
                'decode_responses': True,
            },
        },
    },
    'sample': {
        'BACKEND': 'django_redis_sentinel.cache.RedisSentinelCache',
        'LOCATION': [
            ('127.0.0.1', 26380),
            ('127.0.0.1', 26381),
            ('127.0.0.1', 26382),
        ],
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis_sentinel.client.SentinelClient',
            'SENTINEL_SERVICE_NAME': 'rmaster',
            'REDIS_CLIENT_KWARGS': {
                'db': 1,
                'decode_responses': True,
            },
        },
    },
    'with_prefix': {
        'BACKEND': 'django_redis_sentinel.cache.RedisSentinelCache',
        'LOCATION': [
            ('127.0.0.1', 26380),
            ('127.0.0.1', 26381),
            ('127.0.0.1', 26382),
        ],
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis_sentinel.client.SentinelClient',
            'SENTINEL_SERVICE_NAME': 'rmaster',
            'REDIS_CLIENT_KWARGS': {
                'db': 1,
                'decode_responses': True,
            },
        },
        'KEY_PREFIX': 'test-prefix',
    },
}

INSTALLED_APPS = (
    'django.contrib.sessions',
    'redis_backend_testapp',
    'hashring_test',
)
