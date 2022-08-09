from http.client import HTTPResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from django.views.generic import ListView
from .models import *
from .forms import *
from .utils import get_client_ip
from django.core.exceptions import PermissionDenied


class Blog(ListView):
    template_name = 'blog.html'
    paginate_by = 10
    model = Article

def article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    comments = article.comments.all()
    comment_count = article.comments.count()
    new_comment = None
    comment_form = CommentForm(data=request.POST or None)
    redirect_url = request.META.get("HTTP_REFERER")

    if request.method == 'POST':
        parent_id = request.POST.get("parent-id")
        main_parent_id = request.POST.get("main-parent-id")
        if main_parent_id != "null":
            main_parent_id = int(main_parent_id)
        else:
            main_parent_id = None
        if parent_id != "null":
            parent_id = int(parent_id)
        else: 
            parent_id = None
        parent = Comment.objects.filter(pk=parent_id).first()
        main_parent = Comment.objects.filter(pk=main_parent_id).first()

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.parent = parent
            new_comment.main_parent = main_parent
            new_comment.save()
            return redirect(redirect_url)
    context = {
        'article':article,
        'comments':comments,
        'new_comment':new_comment,
        'comment_form':comment_form,
        'comment_count':comment_count,
    }

    return render(request,'article.html', context)