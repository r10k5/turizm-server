from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.db.models import Q, Count

from turizm_core.forms.zakaz_form import ZakazForm
from turizm_core.models import Zakaz
from turizm_core.helpers import has_role
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

class OrdersView(LoginRequiredMixin, ListView):
    model = Zakaz
    template_name = "zakaz/orders_view.html"
    context_object_name = "zakazy"

    def get_queryset(self):
        if self.request.user.role.id == 'manager':
            manager = self.request.user.polzovatel_set.first()
        elif self.request.user.role.id == 'tour_operator':
            turoperator = self.request.user.turoperator_set.first()

        filter = self.request.GET.get('filter', 'all')

        vse_zakazi = Zakaz.objects.all().annotate(polzovateley_count=Count('zakazpolzovatel'))

        if self.request.user.role.id == 'manager':
            vse_zakazi = vse_zakazi.filter(manager=manager)
        elif self.request.user.role.id == 'tour_operator':
            vse_zakazi = vse_zakazi.filter(putevka__turoperator=turoperator, status__in=[2, 4, 6])

        if filter == 'pending':
            vse_zakazi = vse_zakazi.filter(status__in=[0, 1, 2, 3])
        if filter == 'confirmed':
            vse_zakazi = vse_zakazi.filter(status__in=[4, 5])
        if filter == 'canceled':
            vse_zakazi = vse_zakazi.filter(status=6)

        if self.request.user.role.id in ['manager', 'admin']:
            q = self.request.GET.get('q', '')
            if q:
                vse_zakazi = vse_zakazi.filter(Q(dop_info__icontains=q)|Q(putevka__putevkapolzovatel__polzovatel__familiya__icontains=q)|Q(putevka__putevkapolzovatel__polzovatel__imya__icontains=q)|Q(putevka__putevkapolzovatel__polzovatel__otchestvo__icontains=q))

        return vse_zakazi
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', 'all')
        return context

@method_decorator(has_role(['manager', 'admin']), name='dispatch')
class ManagerOrdersView(LoginRequiredMixin, ListView):
    model = Zakaz
    template_name = "zakaz/orders_view.html"
    context_object_name = "zakazy"

    def get_queryset(self):
        if self.request.user.role.id == 'manager':
            manager = self.request.user.polzovatel_set.first()
        
        filter = self.request.GET.get('filter', 'all')
        
        if self.request.user.role.id == 'manager':
            vse_zakazi = Zakaz.objects.filter(manager=manager)
        elif self.request.user.role.id == 'admin':
            vse_zakazi = Zakaz.objects.all()

        vse_zakazi = vse_zakazi.annotate(polzovateley_count=Count('zakazpolzovatel'))

        if filter == 'pending':
            vse_zakazi = vse_zakazi.filter(status=2)
        if filter == 'confirmed':
            vse_zakazi = vse_zakazi.filter(status=4)
        if filter == 'canceled':
            vse_zakazi = vse_zakazi.filter(status=6)

        q = self.request.GET.get('q', '')
        if q:
            vse_zakazi = vse_zakazi.filter(Q(dop_info__icontains=q))

        return vse_zakazi
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', 'all')
        context['q'] = self.request.GET.get('q', '')
        return context