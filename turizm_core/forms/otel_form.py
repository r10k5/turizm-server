from django import forms
from turizm_core.models import Otel

class OtelForm(forms.ModelForm):
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
        error_messages = {
            "address": {
                "required": "Это поле обязательное"
            },
            "nazvanie": {
                "required": "Это поле обязательное"
            },
            "opisanie": {
                "required": "Это поле обязательное"
            },
            "kolichestvo_zvezd": {
                "required": "Это поле обязательное"
            },
            "osobennosti": {
                "required": "Это поле обязательное"
            },
            "photo": {
                "required": "Это поле обязательное"
            },
        }
