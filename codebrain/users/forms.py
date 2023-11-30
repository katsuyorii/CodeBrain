from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "input-login",
        'placeholder': "Логин",
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "input-login",
        'placeholder': "Пароль",
    }))

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
