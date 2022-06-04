from django.db import models

# Create your models here.


class CategoryJob(models.Model):
    name = models.CharField("Название", max_length=50, unique=True,default="Some String")
    slug = models.SlugField("Слаг", max_length=60, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Job(models.Model):
    name = models.CharField('Название работы', max_length=150, blank=False,default="Some String")
    salary = models.TextField('Зарплата')
    type_of_work = models.CharField('Тип работы', max_length=150, blank=False)
    description = models.CharField('Описание', max_length=500, blank=False)
    category = models.ForeignKey(CategoryJob, on_delete=models.PROTECT,related_name="job")
    slug = models.SlugField("Слаг", max_length=80, unique=True)