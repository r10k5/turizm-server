from django.views.generic import CreateView
from turizm_core.forms.otel_form import OtelForm

class OtelCreateView(CreateView):
    form_class = OtelForm
    template_name = "otel/create_view.html"
    success_url = "/"