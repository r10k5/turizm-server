from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import CreateView, DeleteView, UpdateView, ListView

from turizm_core.forms.polzovatel import PolzovatelManagerForm
from turizm_core.models import Polzovatel

class PolzovatelCreateView(CreateView):
    form_class = PolzovatelManagerForm
    template_name = "polzovatel/create_polzovatel_form.html"
    success_url = "/polzovateli"

class PolzovatelUpdateView(UpdateView):
    form_class = PolzovatelManagerForm
    model = Polzovatel
    template_name = "polzovatel/update_view.html"
    success_url = "/polzovateli"

class PolzovatelDeleteView(DeleteView):
    model = Polzovatel
    success_url = "/polzovateli"

class PolzovatelView(LoginRequiredMixin, ListView):
    model = Polzovatel
    template_name = "polzovatel/polzovatel_view.html"
    context_object_name = "polzovateli"

    def get_queryset(self):
        q = self.request.GET.get("q", "")
        polzovateli = Polzovatel.objects.filter(Q(familia__icontains=q) | Q(imya__icontains=q) | Q(otchestvo__icontains=q))

        if self.request.user.role.id == "manager":
            polzovateli = polzovateli.filter(dannie_autorizatsii__isnull=True)

        return polzovateli
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q", "")
        return context
