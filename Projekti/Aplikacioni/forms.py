from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
     

    class Meta:
        model = User
        fields = ['username' , 'email' , 'password']

class LoginForm(AuthenticationForm):
     username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
     password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))