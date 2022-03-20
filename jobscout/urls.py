from importlib import import_module
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.urls import re_path as url
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'^jet/', include('jet.urls', 'jet')), # Django JET URLS
    # url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')), # Django JET dashboard URLS
    path('', include('appfront.urls')),
    path('jobs/', include('joblist.urls')),
    path('career-notes/', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
