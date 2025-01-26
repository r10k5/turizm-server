from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from turizm_core.forms.auth_form import CustomAuthForm

def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
    else:
        if request.user.is_authenticated:
            return redirect('/')
        form = CustomAuthForm()
    return render(request, 'login.html', {'form': form}) 