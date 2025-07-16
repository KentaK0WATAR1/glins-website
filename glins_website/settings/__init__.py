# glins_website/settings/__init__.py
"""
環境ごとに base → local / prod の順で設定を上書きする。
"""

from .base import *          # まず共通設定を読み込む

# 環境変数 DJANGO_ENV=prod のときだけ prod.py を読む、なども可
try:
    from .local import *     # 開発用の追加設定（存在しなければ無視）
except ImportError:
    pass