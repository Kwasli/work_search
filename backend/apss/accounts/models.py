from django.db import models

# Create your models here.

class User:
    name = models.CharField('Имя', max_length=150, blank=True)
    last_name = models.CharField('Фомилия', max_length=150, blank=True)
    middle_name = models.CharField('Отчество', max_length=150, blank=True)
    email = models.EmailField("Email", unique=True)
    phone = models.CharField('Номер телефона',null=True,max_length=10)
    work_status = models.CharField('Статус работы', max_length=1000, blank=True)