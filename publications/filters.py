# publications/filters.py
import django_filters as filters
from django.db.models import Q
from .models import Publication

class PublicationFilter(filters.FilterSet):
    q = filters.CharFilter(
        label="Keyword",
        method="search",
        widget=filters.widgets.forms.TextInput(
            attrs={"placeholder": "title / author / DOI"}
        ),
    )
    # … year, type などは前回例と同じ …

    def search(self, queryset, name, value):
        """キーワードが空なら絞り込まずそのまま返す"""
        if not value.strip():
            return queryset                    # ←★ここがポイント
        return queryset.filter(
            Q(title__icontains=value) |
            Q(authors__icontains=value) |
            Q(doi__icontains=value)
        )