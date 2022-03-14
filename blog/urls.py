from django.urls import path
from .views import *

urlpatterns = [
    path('', Blog.as_view(), name='blog'),
    path('<slug:slug>', article, name='article')
    
]