from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView
from turizm_core.forms.address_form import AddressForm
from turizm_core.models import Address

class AddressCreateFormView(CreateView):
    form_class = AddressForm
    template_name = "address/create_view.html"
    success_url = "/addressa"
    
class AddressUpdateFormView(UpdateView):
    form_class = AddressForm
    model = Address
    template_name = "address/update_view.html"
    success_url = "/addressa"

class AddressDeleteFormView(DeleteView):
    model = Address
    success_url = "/addressa"

class AddressView(View):
    def get(self, request, *args, **kwargs):
        addressa = Address.objects.all()

        return render(
            request,
            "address/address_view.html",
            {
                "addressa": addressa,
            }
        )