from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
from .models import Article

# Create your views here.

class Blog(ListView):
    template_name = 'blog.html'
    paginate_by = 1
    model = Article

class ArticleView(DetailView):
    model = Article
    template_name = 'article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
