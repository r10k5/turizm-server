from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.db.models import Count
    
from turizm_core.forms.zakaz_form import ZakazForm
from turizm_core.models import Zakaz
from turizm_core.helpers import is_manager

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
    
@method_decorator(is_manager, name='dispatch')
class ManagerOrdersView(LoginRequiredMixin, ListView):
    model = Zakaz
    template_name = "zakaz/orders_view.html"
    context_object_name = "zakazy"

    def get_queryset(self):
        manager = self.request.user.polzovatel_set.first()
        filter = self.request.GET.get('filter', 'all')
        vse_zakazi = Zakaz.objects.filter(manager=manager, status__in=[2, 4, 6]).annotate(polzovateley_count=Count('zakazpolzovatel'))

        if filter == 'pending':
            vse_zakazi = vse_zakazi.filter(status=2)
        if filter == 'confirmed':
            vse_zakazi = vse_zakazi.filter(status=4)
        if filter == 'canceled':
            vse_zakazi = vse_zakazi.filter(status=6)

        return vse_zakazi
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', 'all')
        return context