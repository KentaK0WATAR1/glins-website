#!/usr/bin/env bash
set -e

echo "[entrypoint] Migrating DB…"
python manage.py migrate --noinput

# ---- 初回だけ fixture を流し込む（存在チェック付き） ----
python <<'PY'
import os, django, subprocess, pathlib, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "glins_website.settings")
django.setup()

from publications.models import Publication
from news.models import News  # news アプリを使っていないなら削除

if not Publication.objects.exists() or not News.objects.exists():
    print("[entrypoint] Loading initial fixtures…")
    fx = pathlib.Path(__file__).parent / "fixtures"
    sys.exit(subprocess.call([
        "python", "manage.py", "loaddata",
        fx / "initial_data.json",
        fx / "initial_news.json"
    ]))
print("[entrypoint] Fixtures already present; skip.")
PY
# ---------------------------------------------------------

echo "[entrypoint] Launching Gunicorn…"
exec gunicorn glins_website.wsgi:application --log-file -