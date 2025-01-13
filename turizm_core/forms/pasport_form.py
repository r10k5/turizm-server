from django import forms
from django.forms import ModelForm

from turizm_core.models import Pasport


class PasportForm(ModelForm):
    data_rojdenia = forms.DateField(
        widget=forms.DateInput(attrs={ "type": "date" }, format="%Y-%m-%d"),
        input_formats=["%Y-%m-%d"],
        label="Дата рождения",
        error_messages={
            "required": "Это поле обязательное",
            "invalid": "Должна быть указана корректная дата"
        }
    )
    data_vidachi = forms.DateField(
        widget=forms.DateInput(attrs={ "type": "date" }, format="%Y-%m-%d"),
        input_formats=["%Y-%m-%d"],
        label="Дата выдачи",
        error_messages={
            "required": "Это поле обязательное",
            "invalid": "Должна быть указана корректная дата"
        }
    )

    class Meta:
        model = Pasport
        fields = [
            "familia",
            "imya",
            "otchestvo",
            "data_rojdenia",
            "seria",
            "nomer",
            "data_vidachi",
            "organ_vidachi",
            "scan_pasporta",
        ]
        labels = {
            "familia": "Фамилия",
            "imya": "Имя",
            "otchestvo": "Отчество",
            "seria": "Серия",
            "nomer": "Номер",
            "organ_vidachi": "Орган выдачи",
            "scan_pasporta": "Скан",
        }
        error_messages = {
            "familia": {
                "required": "Это поле обязательное"
            },
            "imya": {
                "required": "Это поле обязательное"
            },
            "otchestvo": {
                "required": "Это поле обязательное"
            },
            "seria": {
                "required": "Это поле обязательное"
            },
            "nomer": {
                "required": "Это поле обязательное"
            },
            "organ_vidachi": {
                "required": "Это поле обязательное"
            },
            "scan_pasporta": {
                "required": "Это поле обязательное"
            },
        }