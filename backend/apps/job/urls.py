from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('job/<int:pk>/', JobListDetail.as_view(), name='job_detail'),
    path('all/job/', JobListView.as_view(), name='job_list'),
    path('search/', JobSearchView.as_view(), name = 'search')
]