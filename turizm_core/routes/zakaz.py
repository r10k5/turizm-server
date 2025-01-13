from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from turizm_core.forms.zakaz_form import ZakazForm
from turizm_core.models import Zakaz

class ZakazCreateView(CreateView):
    form_class = ZakazForm
    template_name = "zakaz/create_view.html"
    success_url = "/zakazi"

class ZakazUpdateView(UpdateView):
    form_class = ZakazForm
    model = Zakaz
    template_name = "zakaz/update_view.html"
    success_url = "/zakazi"

class ZakazDeleteView(DeleteView):
    model = Zakaz
    success_url = "/zakazi"

class ZakazView(View):
    def get(self, request, *args, **kwargs):
        zakazi = Zakaz.objects.all()

        return render(
            request,
            "zakaz/zakaz_view.html",
            {
                "zakazi": zakazi
            }
        )