from django import forms
from django.forms import ModelForm

from turizm_core.models import Zagranpasport

class ZagranpasportForm(ModelForm):
    data_vidachi = forms.DateField(
        widget=forms.DateInput(attrs={ "type": "date" }, format="%Y-%m-%d"),
        input_formats=["%Y-%m-%d"],
        label="Дата выдачи",
        error_messages={
            "required": "Это поле обязательное",
            "invalid": "Должна быть указана корректная дата"
        }
    )
    data_okonchania = forms.DateField(
        widget=forms.DateInput(attrs={ "type": "date" }, format="%Y-%m-%d"),
        input_formats=["%Y-%m-%d"],
        label="Дата окончания срока",
        error_messages={
            "required": "Это поле обязательное",
            "invalid": "Должна быть указана корректная дата"
        }
    )
    class Meta:
        model = Zagranpasport
        fields = [
            "nomer",
            "data_vidachi",
            "organ_vidachi",
            "data_okonchania",
            "scan_zagranpasporta",
        ]
        labels = {
            "nomer": "Номер",
            "organ_vidachi": "Орган выдачи",
            "scan_zagranpasporta": "Скан",
        }
        error_messages = {
            "nomer": {
                "required": "Это поле обязательное"
            },
            "organ_vidachi": {
                "required": "Это поле обязательное"
            },
            "scan_zagranpasporta": {
                "required": "Это поле обязательное"
            },
        }