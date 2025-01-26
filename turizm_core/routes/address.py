from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.db.models import Q
from turizm_core.forms.address_form import AddressForm
from turizm_core.models import Address

class AddressCreateView(CreateView):
    form_class = AddressForm
    template_name = "address/create_view.html"
    success_url = "/addressa"
    
class AddressUpdateView(UpdateView):
    form_class = AddressForm
    model = Address
    template_name = "address/update_view.html"
    success_url = "/addressa"

class AddressDeleteView(DeleteView):
    model = Address
    success_url = "/addressa"

class AddressView(LoginRequiredMixin, ListView):
    model = Address
    template_name = "address/address_view.html"
    context_object_name = "addressa"

    def get_queryset(self):
        addressa = Address.objects.all()
        
        q = self.request.GET.get('q', '')

        if q:
            addressa = addressa.filter(Q(strana__icontains=q)|Q(gorod__icontains=q))

        return addressa
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context
