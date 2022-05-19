from datetime import datetime
from urllib import request
from django.views.generic import ListView, DetailView
from analytics.mixins import ObjectViewedMixin
from .models import *
from .filters import *
from analytics.models import ObjectViewed

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
    paginate_by = 20
    model = JobCard

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)     
        self.model.objects.filter(deadline__lt=datetime.today().strftime('%Y-%m-%d')).delete()
        return context

class JobDetailView(ObjectViewedMixin,DetailView):
    model = JobCard
    queryset = JobCard.objects.all()
    template_name = 'jobdetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        j_object = JobCard.objects.get(slug=self.kwargs.get('slug'))
        context['views'] = ObjectViewed.objects.filter(object_id=j_object.id).count()
        return context
    
    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        instance = JobCard.objects.get(slug=slug)
        return instance