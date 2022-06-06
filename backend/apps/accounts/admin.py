from django.contrib import admin

# Register your models here.


from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'last_name',
        'middle_name',
        'email',
        'phone',
    ]