"""
ASGI config for notification project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from dotenv import load_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notification.settings')

application = get_asgi_application()
