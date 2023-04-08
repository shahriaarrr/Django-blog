from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Article
# Create your views here.

class Index(ListView):
    model = Article
    queryset = Article.objects.all().order_by("-date")
    template_name = 'blog/home.html'
    paginate_by = 1

class DetailArticleView(DetailView):
    model = Article
    template_name = 'blog/blog_post.html'


class About(View):
    def get(self, request):
        return render(request, 'blog/about.html')
