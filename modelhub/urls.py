from django.urls import path
from . import views
from core.views import PostLoginRedirectView 

app_name = "modelhub"

urlpatterns = [
    path("",                    views.ModelOverviewView.as_view(), name="overview"),
    path("demo/",              views.ModelDemoView.as_view(),      name="demo"),
    path("demo/result/",       views.DemoResultView.as_view(),     name="result")
]