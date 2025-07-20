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
    print("✅ Migrations applied.")
except Exception as e:
    print(f"Migration error: {e}")

# TEMP: Auto-create superuser (for Render deployment)
from django.contrib.auth import get_user_model

User = get_user_model()

try:
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("Faizan", "fk@yahoo.com", "Mighty@Admin755")
        print("✅ Superuser created.")
    else:
        print("ℹ️ Superuser already exists.")
except Exception as e:
    print(f"Superuser creation error: {e}")

# Load WSGI application
application = get_wsgi_application()
