from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from turizm_core.forms.putevka_form import PutevkaForm
from turizm_core.models import Putevka


class PutevkaCreateView(CreateView):
    form_class = PutevkaForm
    template_name = "putevka/create_view.html"
    success_url = "/putevki"

class PutevkaUpdateView(UpdateView):
    form_class = PutevkaForm
    model = Putevka
    template_name = "putevka/update_view.html"
    success_url = "/putevki"

class PutevkaDeleteView(DeleteView):
    model = Putevka
    success_url = "/putevki"

class PutevkaView(View):
    def get(self, request, *args, **kwargs):
        putevki = Putevka.objects.all()

        return render(
            request,
            "putevka/putevka_view.html",
            {
                "putevki": putevki
            }
        )