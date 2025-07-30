# publications/urls.py
from django.urls import path
from publications.views import PublicationListView

app_name = "publications"

urlpatterns = [
    path("", PublicationListView.as_view(), name="list"),
]