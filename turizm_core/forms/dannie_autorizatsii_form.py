from django import forms
from django.forms import ModelForm

from turizm_core.models import DannieAutorizatsii


class DannieAutorizatsiiForm(ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label="Пароль",
        error_messages={
            "required": "Это поле обязательное"
        }
    )
    rabochiy_nomer_telephona = forms.CharField(
        label="Рабочий номер телефона",
        required=False
    )
    rabochiy_emale = forms.CharField(
        label="Рабочая электронная почта",
        required=False
    )

    def save(self, commit=True):
        user = super(DannieAutorizatsiiForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta():
        model = DannieAutorizatsii
        fields = [
            "role",
            "nomer_telephona",
            "rabochiy_nomer_telephona",
            "rabochiy_emale",
            "password",
            "email",
            "username",
        ]
        labels = {
            "role": "Роль",
            "nomer_telephona": "Номер телефона",
            "email": "Электронная почта",
            "username": "Имя пользователя",
        }
        error_messages = {
            "role": {
                "required": "Это поле обязательное",
            },
            "nomer_telephona": {
                "required": "Это поле обязательное",
                "unique": "Такой номер телефона уже существует"
            },
            "email": {
                "required": "Это поле обязательное",
                "unique": "Такая электронная почта уже существует"
            },
            "username": {
                "required": "Это поле обязательное",
                "unique": "Такой имя пользователя уже существует"
            },
        }