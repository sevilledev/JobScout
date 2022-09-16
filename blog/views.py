from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from django.views.generic import ListView
from .forms import *
from .utils import get_client_ip
from django.core.exceptions import PermissionDenied
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin

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
        ip_address = get_client_ip(request)
        count = Comment.objects.filter(ip_address=ip_address).count()
        print(count)
        if count < 2 and request.POST.get("content") and ip_address!='195.3.221.154' or ip_address!='195.3.221.155':
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
                new_comment.ip_address = ip_address
                new_comment.save()
                return redirect(redirect_url)
        else:
            raise PermissionDenied
    context = {
        'article':article,
        'comments':comments,
        'new_comment':new_comment,
        'comment_form':comment_form,
        'comment_count':comment_count,
    }

    # hitcount logic
    hit_count = get_hitcount_model().objects.get_for_object(article)
    hits = hit_count.hits
    hitcontext = context['hitcount'] = {'pk': hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    if hit_count_response.hit_counted:
        hits = hits + 1
        hitcontext['hit_counted'] = hit_count_response.hit_counted
        hitcontext['hit_message'] = hit_count_response.hit_message
        hitcontext['total_hits'] = hits

    return render(request,'article.html', context)