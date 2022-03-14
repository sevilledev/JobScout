from django_filters import FilterSet
from .models import JobCard


class JobFilter(FilterSet):
    class Meta:
        model = JobCard
        fields = ['category',]

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
            super(JobFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
            self.filters['category'].field.widget.attrs.update({'class': 'selectpicker search-fields'})