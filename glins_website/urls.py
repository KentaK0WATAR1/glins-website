from django.contrib import admin
from django.urls import path, include
from core.views import PostLoginRedirectView 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("publications/", include("publications.urls")),
    path("model/", include("modelhub.urls")), 
    path("accounts/", include("django.contrib.auth.urls")),  # login, logout, password reset
]