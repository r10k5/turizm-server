from django import forms
from django.forms import ModelForm

from turizm_core.models import Putevka

class PutevkaForm(ModelForm):
    data_vremya_otpravlenia = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={ "type": "datetime-local" }, format="%Y-%m-%dT%H:%M"),
        input_formats=["%Y-%m-%dT%H:%M"],
        label="Дата и время отправления",
        error_messages={
            "required": "Это поле обязательное",
            "invalid": "Должна быть указана корректная дата со временем"
        }
    )
    data_vremya_vozvrashenia = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={ "type": "datetime-local" }, format="%Y-%m-%dT%H:%M"),
        input_formats=["%Y-%m-%dT%H:%M"],
        label="Дата и время возвращения",
        error_messages={
            "required": "Это поле обязательное",
            "invalid": "Должна быть указана корректная дата со временем"
        }
    )
    data_vremya_zaselenia = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={ "type": "datetime-local" }, format="%Y-%m-%dT%H:%M"),
        input_formats=["%Y-%m-%dT%H:%M"],
        label="Дата и время заселения",
        error_messages={
            "required": "Это поле обязательное",
            "invalid": "Должна быть указана корректная дата со временем"
        }
    )
    data_vremya_viselenia = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={ "type": "datetime-local" }, format="%Y-%m-%dT%H:%M"),
        input_formats=["%Y-%m-%dT%H:%M"],
        label="Дата и время выселения",
        error_messages={
            "required": "Это поле обязательное",
            "invalid": "Должна быть указана корректная дата со временем"
        }
    )

    class Meta:
        model = Putevka
        fields = [
            "turoperator",
            "otel",
            "data_vremya_otpravlenia",
            "data_vremya_vozvrashenia",
            "stoimost",
            "data_vremya_zaselenia",
            "data_vremya_viselenia",
        ]
        labels = {
            "turoperator": "Туроператор",
            "otel": "Отель",
            "stoimost": "Стоимость (руб.)",
        }
        error_messages = {
            "turoperator": {
                "required": "Это поле обязательное",
            },
            "otel": {
                "required": "Это поле обязательное",
            },
            "stoimost": {
                "required": "Это поле обязательное",
            },
        }