from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


# Create your models here.



# class UserManager(BaseUserManager):
#     def create_user(self, email=None, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The given email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, password, **extra_fields):
#         """
#         Create and save a SuperUser with the given email and password.
#         """
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#         return self.create_user(email, password, **extra_fields)



# class User(AbstractUser):
#     name = models.CharField('Имя', max_length=150, blank=True)
#     last_name = models.CharField('Фомилия', max_length=150, blank=True)
#     middle_name = models.CharField('Отчество', max_length=150, blank=True)
#     email = models.EmailField("Email", unique=True)
#     phone = models.CharField('Номер телефона',null=True,max_length=10)
#     work_status = models.CharField('Статус работы', max_length=1000, blank=True)