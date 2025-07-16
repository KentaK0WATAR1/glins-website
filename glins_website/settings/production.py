from .base import *
import os                 # 既存 base.py を継承

DEBUG = False
SECRET_KEY = os.getenv("SECRET_KEY")           # Render で環境変数注入

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

# データベース（Render の “PostgreSQL (Free)” を利用）
import dj_database_url
DATABASES = {
    "default": dj_database_url.config(
        conn_max_age=600,
        ssl_require=True,
        default=os.getenv("DATABASE_URL")
    )
}

# Static ファイル（WhiteNoise）
STATIC_ROOT = BASE_DIR / "staticfiles"
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")