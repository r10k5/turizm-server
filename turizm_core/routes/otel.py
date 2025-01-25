from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView
from turizm_core.forms.otel_form import OtelForm
from turizm_core.forms.otel_address_form import OtelAddressForm
from turizm_core.models import Otel, Address

class OtelCreateView(CreateView):
    form_class = OtelAddressForm
    template_name = "otel/create_view.html"
    success_url = "/oteli"

    def form_valid(self, form):
        strana = form.cleaned_data.pop('strana')
        gorod = form.cleaned_data.pop('gorod')

        address, created = Address.objects.get_or_create(strana=strana.lower(), gorod=gorod.lower())

        otel = form.save(commit=False)
        otel.address = address
        otel.save()

        return super().form_valid(form)

class OtelUpdateView(UpdateView):
    form_class = OtelAddressForm
    model = Otel
    template_name = "otel/update_view.html"
    success_url = "/oteli"

    def get_initial(self):
        initial = super().get_initial()
        initial['strana'] = self.object.address.strana
        initial['gorod'] = self.object.address.gorod
        return initial

    def form_valid(self, form):
        strana = form.cleaned_data.pop('strana')
        gorod = form.cleaned_data.pop('gorod')

        address, created = Address.objects.get_or_create(strana=strana.lower(), gorod=gorod.lower())

        otel = form.save(commit=False)
        address_strana = otel.address.strana
        address_gorod = otel.address.gorod
        otel.address = address
        otel.save()

        Address.objects.filter(strana=address_strana.lower(), gorod=address_gorod.lower()).exclude(otel__isnull=False).delete()

        return super().form_valid(form)

class OtelDeleteView(DeleteView):
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