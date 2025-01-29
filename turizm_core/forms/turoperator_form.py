from django import forms
from django.forms import ModelForm

from turizm_core.models import DannieAutorizatsii, Turoperator

class TuroperatorForm(ModelForm):
    dannie_autorizatsii = forms.ModelChoiceField(
        queryset=DannieAutorizatsii.objects.filter(role_id="tour_operator"),
        label="Данные авторизации",
        error_messages={
            "required": "Это поле обязательное"
        }
    )
    class Meta:
        model = Turoperator
        fields = [
            "dannie_autorizatsii",
            "inn",
            "kpp",
            "nazvanie_companii",
        ]
        labels = {
            "inn": "ИНН",
            "kpp": "КПП",
            "nazvanie_companii": "Название компании",
        }
        error_messages = {
            "inn": {
                "required": "Это поле обязательное",
            },
            "kpp": {
                "required": "Это поле обязательное",
            },
            "nazvanie_companii": {
                "required": "Это поле обязательное",
            }, 
        }