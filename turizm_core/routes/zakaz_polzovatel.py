from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from turizm_core.forms.zakaz_polzovatel_form import ZakazPolzovatelForm
from turizm_core.models import ZakazPolzovatel

class ZakazPolzovatelCreateView(CreateView):
    form_class = ZakazPolzovatelForm
    template_name = "zakaz_polzovatel/create_view.html"
    success_url = "/zakazi_polzovateley"

class ZakazPolzovatelUpdateView(UpdateView):
    form_class = ZakazPolzovatelForm
    model = ZakazPolzovatel
    template_name = "zakaz_polzovatel/update_view.html"
    success_url = "/zakazi_polzovateley"

class ZakazPolzovatelDeleteView(DeleteView):
    model = ZakazPolzovatel
    success_url = "/zakazi_polzovateley"

class ZakazPolzovatelView(View):
    def get(self, request, *args, **kwargs):
        zakazi_polzovateley = ZakazPolzovatel.objects.all()

        return render(
            request,
            "zakaz_polzovatel/zakaz_polzovatel_view.html",
            { "zakazi_polzovateley": zakazi_polzovateley }
        )