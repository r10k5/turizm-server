from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render, redirect
from django.contrib.auth import login
from turizm_core.forms.auth_form import CustomAuthForm

def login_view(request):
    print(
        "admin",
        make_password("12345678")
    )
    if request.method == 'POST':
        form = CustomAuthForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')  # Замените 'home' на нужный URL
    else:
        form = CustomAuthForm()
    return render(request, 'dannie_autorizatsii/login.html', {'form': form}) 