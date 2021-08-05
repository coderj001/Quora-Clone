import os
from django.conf import settings

from django.core.wsgi import get_wsgi_application

if settings.SERVER_TYPE == 'development':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'Quora.settings.development')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'Quora.settings.production')


application = get_wsgi_application()
