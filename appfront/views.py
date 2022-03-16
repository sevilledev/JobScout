from django.shortcuts import render
from django.views.generic.edit import FormView

from joblist.models import JobCard
from .forms import *

# Create your views here.

def home(request):
    job_count = JobCard.objects.count()
    sliders = Slider.objects.all()
    context = {
        'job_count':job_count,
        'sliders':sliders
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

class Contact(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.save_msg()
        return super().form_valid(form)
