import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hechizos.settings")

application = get_wsgi_application()

try:
    from .heroku_wsgi import *
except ImportError:
    pass
