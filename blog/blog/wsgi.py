"""
WSGI config for blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import django
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')

# Initialize Django
django.setup()

# Run migrations automatically during WSGI startup
try:
    call_command('migrate', interactive=False)
except Exception as e:
    print(f"Migration error: {e}")

application = get_wsgi_application()
