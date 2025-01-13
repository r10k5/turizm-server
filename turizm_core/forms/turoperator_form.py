from django.forms import ModelForm

from turizm_core.models import Turoperator

class TuroperatorForm(ModelForm):
    class Meta:
        model = Turoperator
        fields = [
            "dannie_autorizatsii",
            "inn",
            "kpp",
            "nazvanie_companii",
        ]
        labels = {
            "dannie_autorizatsii": "Данные авторизации",
            "inn": "ИНН",
            "kpp": "КПП",
            "nazvanie_companii": "Название компании",
        }
        error_messages = {
            "dannie_autorizatsii": {
                "required": "Это поле обязательное",
            },
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