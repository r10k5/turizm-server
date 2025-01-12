"""
URL configuration for turizm_kursovaya project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from turizm_core import views
from turizm_core.routes import address, otel, pasport, role

urlpatterns = [
    path("", views.index),

    path("otel", otel.OtelCreateView.as_view()),
    path("oteli", otel.OtelView.as_view()),
    path("oteli/<int:pk>", otel.OtelUpdateView.as_view()),
    path("otel/delete/<int:pk>", otel.OtelDeleteView.as_view()),

    path("address", address.AddressCreateView.as_view()),
    path("addressa", address.AddressView.as_view()),
    path("address/delete/<int:pk>", address.AddressDeleteView.as_view()),
    path("adressa/<int:pk>", address.AddressUpdateView.as_view()),

    path("role", role.RoleCreateView.as_view()),
    path("roli", role.RoleView.as_view()),
    path("role/delete/<int:pk>", role.RoleDeleteView.as_view()),
    path("roli/<int:pk>", role.RoleUpdateView.as_view()),

    path("pasport", pasport.PasportCreateView.as_view()),
    path("pasporta", pasport.PasportView.as_view()),
    path("pasport/delete/<int:pk>", pasport.PasportDeleteView.as_view()),
    path("pasporta/<int:pk>", pasport.PasportUpdateView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
