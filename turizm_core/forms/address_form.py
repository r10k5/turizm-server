from django import forms

from turizm_core.models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["strana", "gorod"]
        labels = {
            "strana": "Страна",
            "gorod": "Город",
        }