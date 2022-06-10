from django.shortcuts import render
# Create your views here.
from .models import *
from django.views.generic import TemplateView, DetailView

class IndexPage(TemplateView):
    template_name = "index.html"



class JobDetailView(DetailView):
    model = Job
    template_name = "job_detail.html"
    context_object_name = "job"