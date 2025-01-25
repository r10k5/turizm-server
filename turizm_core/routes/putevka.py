from io import BytesIO
from django import forms
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

    
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from fpdf import FPDF
from turizm_core.forms.putevka_form import PutevkaForm
from turizm_core.models import Putevka


class PutevkaCreateView(CreateView):
    form_class = PutevkaForm
    template_name = "putevka/create_view.html"
    success_url = "/putevki"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if self.request.user.role.id == 'tour_operator':
            form.fields['turoperator'].initial = self.request.user.turoperator_set.first()
            form.fields['turoperator'].widget = forms.HiddenInput()
        return form

class PutevkaUpdateView(UpdateView):
    form_class = PutevkaForm
    model = Putevka
    template_name = "putevka/update_view.html"
    success_url = "/putevki"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if self.request.user.role.id == 'tour_operator':
            form.fields['turoperator'].initial = self.request.user.turoperator_set.first()
            form.fields['turoperator'].widget = forms.HiddenInput()
        return form

class PutevkaDeleteView(DeleteView):
    model = Putevka
    success_url = "/putevki"

class PutevkaView(View):
    def get(self, request, *args, **kwargs):
        if request.user.role.id == 'tour_operator':
            putevki = Putevka.objects.filter(turoperator=request.user.turoperator_set.first())
        else:
            putevki = Putevka.objects.all()

        return render(
            request,
            "putevka/putevka_view.html",
            {
                "putevki": putevki
            }
        )

class PutevkaReportView(View):
    def get(self, request, *args, **kwargs):
        if request.user.role.id != 'tour_operator':
            return HttpResponseForbidden("Доступ запрещён")

        putevki = Putevka.objects.filter(turoperator=request.user.turoperator_set.first())

        # Создание PDF
        buffer = BytesIO()
        pdf = FPDF()
        pdf.add_page()
        pdf.add_font('Roboto', '', 'Roboto.ttf', uni=True)
        pdf.set_font('Roboto', '', 9)

        pdf.cell(200, 10, txt="Отчёт по продажам путёвок", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Туроператор: {request.user.username}", ln=True, align='C')

        pdf.ln(10)  # Пустая строка

        # Заголовки таблицы
        pdf.cell(30, 10, 'Идентификатор', 1)
        pdf.cell(50, 10, 'Страна', 1)
        pdf.cell(50, 10, 'Город', 1)
        pdf.cell(30, 10, 'Продаж', 1)
        pdf.cell(30, 10, 'Сумма', 1)
        pdf.ln()

        for putevka in putevki:
            kolichestvo_lyudey = 0
            for zakaz in putevka.zakaz_set.all():
                kolichestvo_lyudey += zakaz.zakazpolzovatel_set.count()
            
            summa = kolichestvo_lyudey * putevka.stoimost

            pdf.cell(30, 10, str(putevka.id), 1)
            pdf.cell(50, 10, putevka.otel.address.strana, 1)
            pdf.cell(50, 10, putevka.otel.address.gorod, 1)
            pdf.cell(30, 10, str(kolichestvo_lyudey), 1)
            pdf.cell(30, 10, str(summa), 1)
            pdf.ln()

        pdf.output(buffer)
        buffer.seek(0)

        return HttpResponse(buffer, content_type='application/pdf', headers={'Content-Disposition': 'attachment; filename="report.pdf"'})
