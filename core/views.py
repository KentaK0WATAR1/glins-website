from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
# Create your views here.


class HomeView(TemplateView):
    template_name = "core/home.html"

class AboutView(TemplateView):
    template_name = "core/about.html"

class TeamView(TemplateView):
    template_name = "core/team.html"

class ContactView(TemplateView):
    template_name = "core/contact.html"

class PostLoginRedirectView(LoginRequiredMixin, View):
    """
    ログイン直後の振り分け。
    demo → modelhub:demo
    それ以外 → ホーム
    """
    def get(self, request, *args, **kwargs):
        if request.user.username.lower() == "demo":
            return redirect("modelhub:demo")
        return redirect("core:home")        # 好きなデフォルト先