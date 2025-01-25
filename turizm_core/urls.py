from django.urls import path
from .routes import otel

urlpatterns = [
    path('oteli/create/', otel.OtelCreateView.as_view(), name='otel_create'),
    # другие пути...
] 