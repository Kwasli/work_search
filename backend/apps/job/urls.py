from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
]