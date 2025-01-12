from django import forms
from django.forms import ModelForm

from turizm_core.models import Polzovatel


class PolzovatelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PolzovatelForm, self).__init__(*args, **kwargs)

        self.fields["pasport"].required = False
        self.fields["zagranpasport"].required = False


    class Meta:
        model = Polzovatel
        fields = [
            "dannie_autorizatsii",
            "pasport",
            "zagranpasport",
        ]
        labels = {
            "dannie_autorizatsii": "Данные авторизации",
            "pasport": "Паспорт",
            "zagranpasport": "Загранпаспорт",
        }
        error_messages = {
            "dannie_autorizatsii": {
                "required": "Это поле обязательное"
            }
        }
