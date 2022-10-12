from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def login_view(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(f'/{username}')
        else:
            messages.success(request, ('There was an error... Please try again.'))
            return render(request, 'auth/login.html', {})
    else:
        if request.user.is_authenticated:
            return redirect(f'/{request.user.username}')
        return render(request, 'auth/login.html', {})


def loggedin_view(request, username):
    if username == request.user.username:
        return render(request, 'user/home.html', {"username": request.user.username})
    return redirect('log_in')


def logout_view(request):
    logout(request)
    messages.success(request, ('You have been logged out!'))
    return redirect('log_in')


def register_user(request):
    return render(request, 'auth/register_user.html')