from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

from turizm_core.helpers import is_tour_operator

from turizm_core.forms.turoperator_form import TuroperatorForm
from turizm_core.models import Turoperator, Zakaz

class TuroperatorCreateView(CreateView):
    form_class = TuroperatorForm
    template_name = "turoperator/create_view.html"
    success_url = "/turoperatori"

class TuroperatorUpdateView(UpdateView):
    form_class = TuroperatorForm
    model = Turoperator
    template_name = "turoperator/update_view.html"
    success_url = "/turoperatori"

class TuroperatorDeleteView(DeleteView):
    model = Turoperator
    success_url = "/turoperatori"

class TuroperatorView(View):
    def get(self, request, *args, **kwargs):
        turoperatori = Turoperator.objects.all()

        return render(
            request,
            "turoperator/turoperator_view.html",
            {
                "turoperatori": turoperatori
            }
        )

@method_decorator(is_tour_operator, name='dispatch')
class TuroperatorOrdersView(LoginRequiredMixin, ListView):
    model = Zakaz
    template_name = "turoperator/orders_view.html"
    context_object_name = "zakazy"

    def get_queryset(self):
        turoperator = self.request.user.turoperator_set.first()
        return Zakaz.objects.filter(putevka__turoperator=turoperator)