from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from turizm_core.forms.dannie_autorizatsii_form import DannieAutorizatsiiForm
from turizm_core.models import DannieAutorizatsii

class DannieAutorizatsiiCreateView(CreateView):
    form_class = DannieAutorizatsiiForm
    template_name = "dannie_autorizatsii/create_view.html"
    success_url = "/dannie-autorizatsii"

class DannieAutorizatsiiUpdateView(UpdateView):
    form_class = DannieAutorizatsiiForm
    model = DannieAutorizatsii
    template_name = "dannie_autorizatsii/update_view.html"
    success_url = "/dannie-autorizatsii"

class DannieAutorizatsiiDeleteView(DeleteView):
    model = DannieAutorizatsii
    success_url = "/dannie-autorizatsii"

class DannieAutorizatsiiView(View):
    def get(self, request, *args, **kwargs):
        dannie = DannieAutorizatsii.objects.all()

        return render(
            request,
            "dannie_autorizatsii/dannie_view.html",
            {
                "dannie": dannie,
            }
        )