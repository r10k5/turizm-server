from django.forms import ModelForm

from turizm_core.models import Role

class RoleForm(ModelForm):
    class Meta:
        model = Role
        fields = ["id", "opisanie"]
        labels = {
            "id": "Идентификатор роли",
            "opisanie": "Описание роли"
        }
        error_messages = {
            "id": {
                "unique": "Такая роль уже существует",
                "required": "Это поле обязательно для заполнения",
            },
            "opisanie": {
                "required": "Это поле обязательно для заполнения",
            }
        }