"""
WSGI config for sidewinderjoe project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os, sys

sys.path.append("/var/www/env/sidewinderjoe")

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sidewinderjoe.settings")

application = get_wsgi_application()
