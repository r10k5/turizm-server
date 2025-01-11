from django import forms
from turizm_core.models import Otel

class CreateOtelForm(forms.ModelForm):
    class Meta:
        model = Otel
        fields = [
            "nazvanie",
            "opisanie",
            "kolichestvo_zvezd",
            "osobennosti",
            "photo",
            "address",
        ]
        labels = {
            "address": "Адрес",
            "nazvanie": "Название",
            "opisanie": "Описание",
            "kolichestvo_zvezd": "Количество звёзд",
            "osobennosti": "Особенности",
            "photo": "Фотография отеля"
        }
