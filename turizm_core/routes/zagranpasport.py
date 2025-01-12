from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from turizm_core.forms.zagranpasport import ZagranpasportForm
from turizm_core.models import Zagranpasport

class ZagranpasportCreateView(CreateView):
    form_class = ZagranpasportForm
    template_name = "zagranpasport/create_view.html"
    success_url = "/zagranpasporta"

class ZagranpasportUpdateView(UpdateView):
    form_class = ZagranpasportForm
    model = Zagranpasport
    template_name = "zagranpasport/update_view.html"
    success_url = "/zagranpasporta"

class ZagranpasportDeleteView(DeleteView):
    model = Zagranpasport
    success_url = "/zagranpasporta"

class ZagranpasportView(View):
    def get(self, request, *args, **kwargs):
        zagranpasporta = Zagranpasport.objects.all()

        return render(
            request,
            "zagranpasport/zagranpasport_view.html",
            { "zagranpasporta": zagranpasporta }
        )