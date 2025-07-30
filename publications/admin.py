from django.contrib import admin
from .models import Publication


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display  = ("title", "year", "type")
    list_filter   = ("year", "type")
    search_fields = ("title", "authors", "doi")
    ordering      = ("-year", "title")