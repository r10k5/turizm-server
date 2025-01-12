from django.forms import ModelForm

from turizm_core.models import Role

class RoleForm(ModelForm):
    class Meta:
        model = Role
        fields = ["opisanie"]
        labels = {
            "opisanie": "Название роли"
        }
        error_messages = {
            "opisanie": {
                "required": "Это поле обязательно для заполнения",
            }
        }