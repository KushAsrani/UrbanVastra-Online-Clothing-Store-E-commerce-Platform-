"""
WSGI config for genx project.
"""

import os
import sys
from pathlib import Path

# The repository layout is:
# repository/
# ├── api/
# └── genx/
#     └── genx/
#
# Add the outer genx directory so "genx.settings" can be imported.
PROJECT_DIR = Path(__file__).resolve().parent.parent

if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "genx.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()