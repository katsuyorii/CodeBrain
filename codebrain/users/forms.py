from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
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


class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "input-login",
    }))

    email = forms.CharField(required=False, widget=forms.EmailInput(attrs={
        'class': "input-login",
    }))

    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        'type': 'file',
        'name': 'file',
    }))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'image',
        ]


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "input-login",
        'placeholder': "Логин",
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "input-login",
        'placeholder': "Пароль",
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "input-login",
        'placeholder': "Повторите пароль",
    }))

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]