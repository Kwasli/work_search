from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={'class':'form-styling'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-styling'}))
    



class UserRegisterForm(UserCreationForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class':'form-styling'}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class':'form-styling'}
        )
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-styling'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-styling'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-styling'}))
    middle_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-styling'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-styling'}))

    

    class Meta:
        model = User
        fields = [
            'email',
            'name',
            'last_name',
            'middle_name',
            'phone',
        ]

    def clean_passwor2(self):
        cd  = self.cleaned_data
        if cd ['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']


class UserEntryForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    middle_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
