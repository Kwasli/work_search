from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json
from .models import *

def get_category(request):
    id = request.GET.get('id', '')
    result = list(CategoryJob.objects.filter(
    category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")