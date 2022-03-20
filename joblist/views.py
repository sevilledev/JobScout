from django.views.generic import ListView, DetailView
from multiprocessing import context
from django.shortcuts import render
from .models import *
from .filters import *

# Create your views here.

class FilteredListView(ListView):
    filterset_class = None

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class JobListView(FilteredListView):
    filterset_class = JobFilter
    template_name = 'joblist.html'
    paginate_by = 5
    model = JobCard

class JobDetailView(DetailView):
    model = JobCard
    template_name = 'jobdetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context