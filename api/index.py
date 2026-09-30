import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
GENX_ROOT = PROJECT_ROOT / "genx"

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

if str(GENX_ROOT) not in sys.path:
    sys.path.insert(0, str(GENX_ROOT))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "genx.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()