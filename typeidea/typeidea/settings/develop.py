from .base import  * # NOQA
# # NOQA是高数PEP 8规范工具这个地方不用监测

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}