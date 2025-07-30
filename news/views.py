from django.views.generic import ListView, DetailView
from .models import News


class NewsListView(ListView):
    template_name = "news/news_list.html"
    context_object_name = "news_list"
    paginate_by = 9
    queryset = News.objects.all()


class NewsDetailView(DetailView):
    template_name = "news/news_detail.html"
    context_object_name = "news"
    model = News