from django.views.generic import ListView, DetailView
from multiprocessing import context
from django.shortcuts import render
from .models import *

# Create your views here.

class JobListView(ListView):
    template_name = 'joblist.html'
    paginate_by = 2
    model = JobCard

class JobDetailView(DetailView):
    model = JobCard
    template_name = 'jobdetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context