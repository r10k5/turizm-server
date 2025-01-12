from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from turizm_core.forms.pasport_form import PasportForm
from turizm_core.models import Pasport

class PasportCreateView(CreateView):
    form_class = PasportForm
    template_name = "pasport/create_view.html"
    success_url = "/pasporta"

class PasportUpdateView(UpdateView):
    form_class = PasportForm
    model = Pasport
    template_name = "pasport/update_view.html"
    success_url = "/pasporta"

class PasportDeleteView(DeleteView):
    model = Pasport
    success_url = "/pasporta"

class PasportView(View):
    def get(self, request, *args, **kwargs):
        pasporta = Pasport.objects.all()

        return render(
            request,
            "pasport/pasport_view.html",
            { "pasporta": pasporta }
        )