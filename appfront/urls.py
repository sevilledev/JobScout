from django.urls import path
from .views import *
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
	path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', Contact.as_view(), name='contact'),
]