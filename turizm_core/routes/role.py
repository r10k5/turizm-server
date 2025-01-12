from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from turizm_core.forms.role_form import RoleForm
from turizm_core.models import Role

class RoleCreateView(CreateView):
    form_class = RoleForm
    template_name = "role/create_view.html"
    success_url = "/roli"

class RoleUpdateView(UpdateView):
    form_class = RoleForm
    model = Role
    template_name = "role/update_view.html"
    success_url = "/roli"

class RoleDeleteView(DeleteView):
    model = Role
    success_url = "/roli"

class RoleView(View):
    def get(self, request, *args, **kwargs):
        roli = Role.objects.all()

        return render(request, "role/role_view.html", { "roli": roli })