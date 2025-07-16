from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ModelOverviewView(TemplateView):
    template_name = "modelhub/overview.html"

@method_decorator(login_required, name="dispatch")
class ModelDemoView(TemplateView):
    template_name = "modelhub/demo.html"

@method_decorator(login_required, name="dispatch")
class DemoResultView(TemplateView):
    template_name = "modelhub/result.html"