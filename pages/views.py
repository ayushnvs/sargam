from django.http import HttpResponse
from django.shortcuts import render, redirect

def home_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect(f'/{request.user.username}')
    return render(request, 'sargam/home.html', {"username": request.user.username})


def about_view(request, *args, **kwargs):
    return render(request, 'sargam/about.html', {"username": request.user.username})


def community_view(request, *args, **kwargs):
    return render(request, 'sargam/community.html', {"username": request.user.username})


def contact_view(request, *args, **kwargs):
    return render(request, 'sargam/contact.html', {"username": request.user.username})
