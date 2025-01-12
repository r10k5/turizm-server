from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView
from turizm_core.forms.otel_form import OtelForm
from turizm_core.models import Otel

class OtelCreateView(CreateView):
    form_class = OtelForm
    template_name = "otel/create_view.html"
    success_url = "/oteli"

class OtelUpdateView(UpdateView):
    form_class = OtelForm
    model = Otel
    template_name = "otel/update_view.html"
    success_url = "/oteli"

class OtelDeleteFormView(DeleteView):
    model = Otel
    success_url = "/oteli"

class OtelView(View):
    def get(self, request, *args, **kwargs):
        oteli = Otel.objects.all()

        return render(
            request,
            "otel/otel_view.html",
            {
                "oteli": oteli,
            }
        )