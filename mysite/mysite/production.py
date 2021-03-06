#!/usr/env/bin python
import os
import dj_database_url

from .settings import *

# this is used when no environment variable is available
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite'))
}

# False = do not print error trace on production website
DEBUG = False
TEMPLATE_DEBUG = False
# security parameter
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS'), 'localhost']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
SECRET_KEY = os.environ.get('SECRET_KEY')