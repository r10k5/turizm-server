from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from turizm_core.forms.polzovatel import PolzovatelForm
from turizm_core.models import Polzovatel

class PolzovatelCreateView(CreateView):
    form_class = PolzovatelForm
    template_name = "polzovatel/create_view.html"
    success_url = "/polzovateli"

class PolzovatelUpdateView(UpdateView):
    form_class = PolzovatelForm
    model = Polzovatel
    template_name = "polzovatel/update_view.html"
    success_url = "/polzovateli"

class PolzovatelDeleteView(DeleteView):
    model = Polzovatel
    success_url = "/polzovateli"

class PolzovatelView(View):
    def get(self, request, *args, **kwargs):
        polzovateli = Polzovatel.objects.all()

        return render(
            request,
            "polzovatel/polzovatel_view.html",
            {
                "polzovateli": polzovateli
            }
        )