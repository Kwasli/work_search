from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(CategoryJob)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name', )}
    






@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'type_of_work',
        'description',
    ]