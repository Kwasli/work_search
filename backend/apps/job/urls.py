from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('all/job/', JobListView.as_view(), name='job_list'),
    path('search/', JobSearchView.as_view(), name = 'search'),
    path('all/job/it/', JobITListView.as_view(), name='job_it_list'),
    path('job/it/<int:pk>/', JobITDetailView.as_view(), name = 'job_it_detail'),
]