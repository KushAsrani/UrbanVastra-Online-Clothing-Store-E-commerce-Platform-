import sys
import os
from pathlib import Path

# Add the genx directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'genx'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'genx.settings')

import django
django.setup()

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()

def handler(request):
    """Vercel serverless function handler"""
    return app(request)