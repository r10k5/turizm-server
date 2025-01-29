from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import CreateView, DeleteView, UpdateView, ListView

from turizm_core.forms.polzovatel import PolzovatelManagerForm
from turizm_core.models import Polzovatel

class PolzovatelCreateView(LoginRequiredMixin, CreateView):
    form_class = PolzovatelManagerForm
    template_name = "polzovatel/create_polzovatel_form.html"
    success_url = "/polzovateli"

    def get_form_kwargs(self):
        print(self.request)
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

class PolzovatelUpdateView(LoginRequiredMixin, UpdateView):
    form_class = PolzovatelManagerForm
    model = Polzovatel
    template_name = "polzovatel/update_view.html"
    success_url = "/polzovateli"

class PolzovatelDeleteView(LoginRequiredMixin, DeleteView):
    model = Polzovatel
    success_url = "/polzovateli"

class PolzovatelView(LoginRequiredMixin, ListView):
    model = Polzovatel
    template_name = "polzovatel/polzovatel_view.html"
    context_object_name = "polzovateli"

    def get_queryset(self):
        filter = self.request.GET.get("filter", "all")

        polzovateli = Polzovatel.objects.all()

        if self.request.user.role.id == "admin":
            if filter == "clients":
                polzovateli = Polzovatel.objects.filter(dannie_autorizatsii__isnull=True)
            elif filter == "managers":
                polzovateli = Polzovatel.objects.filter(dannie_autorizatsii__isnull=False)

        q = self.request.GET.get("q", "")
        polzovateli = polzovateli.filter(Q(familia__icontains=q) | Q(imya__icontains=q) | Q(otchestvo__icontains=q))

        if self.request.user.role.id == "manager":
            polzovateli = polzovateli.filter(dannie_autorizatsii__isnull=True)

        return polzovateli
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q", "")

        if self.request.user.role.id == "admin":
            context["filter"] = self.request.GET.get("filter", "all")
        
        return context
