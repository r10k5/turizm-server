from django import forms
from django.forms import ModelForm

from turizm_core.models import DannieAutorizatsii, Polzovatel


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


class PolzovatelManagerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")

        super(PolzovatelManagerForm, self).__init__(*args, **kwargs)

        if self.request.user.role.id == "manager":
            self.fields.pop("dannie_autorizatsii")

    dannie_autorizatsii = forms.ModelChoiceField(
        queryset=DannieAutorizatsii.objects.filter(role_id__in=["manager", "admin"]),
        label="Данные авторизации",
        error_messages={
            "required": "Это поле обязательное"
        },
        required=False
    )

    class Meta:
        model = Polzovatel
        fields = [
            "dannie_autorizatsii",
            "familia",
            "imya", 
            "otchestvo",
        ]

        labels = {
            "familia": "Фамилия",
            "imya": "Имя",
            "otchestvo": "Отчество",
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
            }
        }
