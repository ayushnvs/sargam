from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_view(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(f'/{username}')
        else:
            return render(request, 'auth/login.html', {})
    else:
        return render(request, 'auth/login.html', {})


def loggedin_view(request, username):
    if username == request.user.username:
        return render(request, 'user/home.html', {"username": request.user.username})
    return redirect('log_in')