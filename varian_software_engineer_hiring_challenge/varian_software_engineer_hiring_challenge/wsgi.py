"""
WSGI config for varian_software_engineer_hiring_challenge project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "varian_software_engineer_hiring_challenge.settings")

application = get_wsgi_application()
