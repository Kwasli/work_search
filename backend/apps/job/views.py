from django.shortcuts import render
# Create your views here.
from .models import *
from django.views.generic import TemplateView, DetailView, ListView

class IndexPage(TemplateView):
    template_name = "index.html"
    context_object_name = "job"



class JobListDetail(DetailView):
    model = Job
    template_name = "job_detail.html"
    context_object_name = "job"

class JobListView(ListView):
    model = Job
    template_name = 'job_list.html'
    context_object_name = 'jobs'


