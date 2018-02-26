from .base import *

DEBUG = False

ALLOWED_HOSTS = ['http://hechizos.herokuapp.com/']

DATABASES = {'default': dj_database_url.config()}
