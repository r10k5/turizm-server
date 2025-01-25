from django import forms
from turizm_core.models import Otel

class OtelAddressForm(forms.ModelForm):
    strana = forms.CharField(label="Страна", max_length=100)
    gorod = forms.CharField(label="Город", max_length=255)

    class Meta:
        model = Otel
        fields = [
            "nazvanie",
            "opisanie",
            "kolichestvo_zvezd",
            "osobennosti",
            "photo",
        ]
        labels = {
            "nazvanie": "Название",
            "opisanie": "Описание",
            "kolichestvo_zvezd": "Количество звёзд",
            "osobennosti": "Особенности",
            "photo": "Фотография отеля"
        }
        error_messages = {
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