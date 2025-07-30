from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from news.models import News
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
    
class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["latest_news"] = News.objects.all()[:3]  # newest 3
        return ctx