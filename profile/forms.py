from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}), label='')


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=25, required=True, widget=forms.TextInput(attrs={'placeholder': 'username'}), label='')
    email = forms.CharField(max_length=50, required=True, widget=forms.EmailInput(attrs={'placeholder': 'email'}), label='')
    password1 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'password'}), label='')
    password2 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'confirm password'}), label='')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
