from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя", max_length=150)
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)

    error_messages = {
        "invalid_login": "Неверное имя пользователя или пароль",
        "inactive": "Аккаунт не активен",
    }