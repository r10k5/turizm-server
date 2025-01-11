from django.http import HttpRequest, HttpResponseNotAllowed
from django.shortcuts import redirect, render
from turizm_core.forms.otel_form import CreateOtelForm

def otel_view(request: HttpRequest):
    if request.method == "GET":
        return render(
            request,
            "otel/create_edit_form.html",
            {
                "is_edit": False,
                "form": CreateOtelForm(),
                "has_error": False,
            }
        )

    if request.method != "POST":
        return HttpResponseNotAllowed("Supports POST only")
    
    otel_form = CreateOtelForm(request.POST, request.FILES)

    if otel_form.is_valid():
        otel_form.save()
        
        return redirect("Index")

    return render(
        request,
        "otel/create_edit_form.html",
        {
            "is_edit": False,
            "form": otel_form,
            "error": True,
        }
    )

    