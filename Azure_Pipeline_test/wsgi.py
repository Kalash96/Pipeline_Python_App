"""
WSGI config for Azure_Pipeline_test project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Azure_Pipeline_test.settings')

path_ = '..\antenv\lib\site-packages\django'

if path_ not in sys.path:
    sys.path.insert(0, path_)

application = get_wsgi_application()
