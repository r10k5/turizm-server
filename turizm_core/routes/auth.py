from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render, redirect
from django.contrib.auth import login
from turizm_core.forms.auth_form import CustomAuthForm

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
    else:
        form = CustomAuthForm()
    return render(request, 'login.html', {'form': form}) 