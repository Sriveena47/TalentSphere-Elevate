import os
from pathlib import Path

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

application = get_wsgi_application()

if os.getenv("VERCEL"):
    from django.core.management import call_command

    call_command("migrate", interactive=False, verbosity=0)
    fixture = Path(__file__).resolve().parent.parent / "demo_data.json"
    if fixture.exists():
        call_command("loaddata", str(fixture), verbosity=0)
