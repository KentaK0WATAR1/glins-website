from django.contrib import admin
from .models import TeamMember


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display  = ("name", "position", "affiliation")   # ← フィールドを実在する3つに
    list_filter   = ("affiliation",)                      # 任意
    search_fields = ("name", "position", "affiliation")