# entrypoint.sh  (chmod +x してコミット)
#!/usr/bin/env bash
set -e

python manage.py migrate --noinput

# ── 1回だけ fixture を流す ────────────────────────────
if [ ! -f .fixtures_loaded ]; then
  echo "[entrypoint] Loading initial fixtures …"
  python manage.py loaddata fixtures/initial_data.json
  touch .fixtures_loaded         # 2 回目以降はスキップ
fi
# ────────────────────────────────────────────────────

exec gunicorn glins_website.wsgi:application --log-file -