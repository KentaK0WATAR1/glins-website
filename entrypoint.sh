#!/usr/bin/env bash
set -e

python manage.py migrate --noinput

# 初期データが無い時だけ fixture を投入
python <<'PY'
import os, django, subprocess, sys, pathlib
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glins_website.settings')
django.setup()
from publications.models import Publication
from news.models import News
if not Publication.objects.exists() or not News.objects.exists():
    print('[init] Loading fixtures …')
    fixtures = pathlib.Path(__file__).parent / "fixtures"
    subprocess.check_call(["python", "manage.py", "loaddata",
                           fixtures / "initial_data.json",
                           fixtures / "initial_news.json"])
PY

gunicorn glins_website.wsgi:application --log-file -