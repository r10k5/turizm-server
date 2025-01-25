from django import forms
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

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