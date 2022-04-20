from django.urls import path
from .views import *

urlpatterns = [
    path('', JobListView.as_view(), name='joblist'),
    path('(?<slug>[\w-])+/', JobDetailView.as_view(), name='jobdetail')
]