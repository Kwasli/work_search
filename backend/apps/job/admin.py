from django.contrib import admin

# Register your models here.

from .models import *






@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'salary',
        'requirements',
        'responsibilities',
        'working_conditions',
        'an_experience',
        'schedule',
        'education',
    ]


@admin.register(JobIT)
class JobITAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'salary',
        'requirements',
        'responsibilities',
        'working_conditions',
        'an_experience',
        'schedule',
        'education',
    ]