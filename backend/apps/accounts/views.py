from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView, TemplateView
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
# Create your views here.
from .forms import *

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm


    def form_valid(self, form):
        data = form.cleaned_data
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('index')

            else:
                return HttpResponse('Ваш аккаунт неактивен')
        return HttpResponse('такого юзера не сушествует')



class UserRegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserRegisterForm
    success_url = '/'

class RegisterDoneView(TemplateView):
    template_name = "register_done.html"

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')