from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from io import BytesIO
from fpdf import FPDF

from turizm_core.helpers import is_admin, is_tour_operator

from turizm_core.forms.turoperator_form import TuroperatorForm
from turizm_core.models import Putevka, Turoperator, Zakaz

class TuroperatorCreateView(CreateView):
    form_class = TuroperatorForm
    template_name = "turoperator/create_view.html"
    success_url = "/turoperatori"

class TuroperatorUpdateView(UpdateView):
    form_class = TuroperatorForm
    model = Turoperator
    template_name = "turoperator/update_view.html"
    success_url = "/turoperatori"

class TuroperatorConfirmOrderView(View):
    def post(self, request, *args, **kwargs):
        zakaz = Zakaz.objects.get(id=kwargs['zakaz_id'])
        zakaz.status = 4
        zakaz.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))

class TuroperatorCancelOrderView(View):
    def post(self, request, *args, **kwargs):
        zakaz = Zakaz.objects.get(id=kwargs['zakaz_id'])
        zakaz.status = 6
        zakaz.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))

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
    template_name = "zakaz/orders_view.html"
    context_object_name = "zakazy"

    def get_queryset(self):
        turoperator = self.request.user.turoperator_set.first()
        filter = self.request.GET.get('filter', 'all')
        vse_zakazi = Zakaz.objects.filter(putevka__turoperator=turoperator, status__in=[2, 4, 6]).annotate(polzovateley_count=Count('zakazpolzovatel'))

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
    
@method_decorator(is_admin, name='dispatch')
class TuroperatorReportView(View):
    def get(self, request, *args, **kwargs):
        turoperatori = Turoperator.objects.all()
        
        # Создание PDF
        buffer = BytesIO()
        pdf = FPDF()
        pdf.add_page()
        pdf.add_font('Roboto', '', 'Roboto.ttf', uni=True)
        pdf.set_font('Roboto', '', 12)
        
        pdf.cell(200, 10, txt="Отчёт по туроператорам", ln=True, align='C')
        pdf.ln(10)
        
        # Заголовки таблицы
        pdf.cell(60, 10, 'Туроператор', 1)
        pdf.cell(40, 10, 'Кол-во путёвок', 1)
        pdf.cell(40, 10, 'Кол-во клиентов', 1)
        pdf.cell(50, 10, 'Общая выручка', 1)
        pdf.ln()
        
        for turoperator in turoperatori:
            putevki = Putevka.objects.filter(turoperator=turoperator, zakaz__status=5)
            total_putevki = putevki.count()
            total_clients = 0
            total_earnings = 0
            
            for putevka in putevki:
                zakazi = Zakaz.objects.filter(putevka=putevka, status=5)
                for zakaz in zakazi:
                    polzovateley = zakaz.zakazpolzovatel_set.count()
                    total_clients += polzovateley
                    total_earnings += putevka.stoimost * polzovateley
            
            # Добавление данных в таблицу
            pdf.cell(60, 10, turoperator.nazvanie_companii, 1)
            pdf.cell(40, 10, str(total_putevki), 1)
            pdf.cell(40, 10, str(total_clients), 1)
            pdf.cell(50, 10, str(total_earnings), 1)
            pdf.ln()
        
        pdf.output(buffer)
        buffer.seek(0)
        
        return HttpResponse(buffer, content_type='application/pdf', headers={'Content-Disposition': 'attachment; filename="turoperator_report.pdf"'})
