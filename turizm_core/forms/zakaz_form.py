from django import forms
from django.forms import ModelForm

from turizm_core.models import STATUSY_ZAKAZA, Zakaz

class ZakazForm(ModelForm):
    status = forms.ChoiceField(
        choices=STATUSY_ZAKAZA.items(),
        label="Статус",
        error_messages={
            "required": "Это поле обязательное"
        }
    )

    def __init__(self, *args, **kwargs):
        super(ZakazForm, self).__init__(*args, **kwargs)

        self.fields["dop_info"].required = False

    class Meta:
        model = Zakaz
        fields = [
            "putevka",
            "status",
            "dop_info",
        ]
        labels = {
            "putevka": "Путёвка",
            "status": "Статус",
            "dop_info": "Дополнительная информация",
        }
        error_messages = {
            "putevka": {
                "required": "Это поле обязательное"
            },
        }