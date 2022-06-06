from django.db import models

# Create your models here.

class Job(models.Model):
    name = models.CharField('Название работы', max_length=150, blank=False,default="Some String")
    salary = models.TextField('Зарплата', default='-----')
    requirements = models.TextField('Требования', default='-----')
    responsibilities = models.TextField('Обязаности', default='-----')
    working_conditions = models.TextField('Условия работы', default='-----')
    an_experience = models.TextField('Опыт Работы', default='-----')
    schedule = models.TextField('График работы', default='-----')
    education = models.TextField('Оброзование', default='-----')
    slug = models.SlugField("Слаг", max_length=80, unique=True)
    