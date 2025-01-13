from django.forms import ModelForm

from turizm_core.models import ZakazPolzovatel

class ZakazPolzovatelForm(ModelForm):
    class Meta:
        model = ZakazPolzovatel
        fields = [
            "zakaz",
            "polzovatel",
            "scan_dogovora",
            "nomer_bileta_tuda",
            "nomer_bileta_obratno",
        ]
        labels = {
            "zakaz": "Заказ",
            "polzovatel": "Пользователь",
            "scan_dogovora": "Скан договора",
            "nomer_bileta_tuda": "Номер билета туда",
            "nomer_bileta_obratno": "Номер билета обратно",
        }
        error_messages = {
            "zakaz": {
                "required": "Это обязательное поле"
            },
            "polzovatel": {
                "required": "Это обязательное поле"
            },
            "scan_dogovora": {
                "required": "Это обязательное поле"
            },
            "nomer_bileta_tuda": {
                "required": "Это обязательное поле"
            },
            "nomer_bileta_obratno": {
                "required": "Это обязательное поле"
            },
        }