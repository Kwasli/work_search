from django.urls import path

from .views import *

urlpatterns = [
    path('getCategory/', get_category, name='get_category')
]