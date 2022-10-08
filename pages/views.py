from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs):
    return render(request, 'sargam/home.html', {})


def about_view(request, *args, **kwargs):
    return render(request, 'sargam/about.html', {})


def community_view(request, *args, **kwargs):
    return render(request, 'sargam/community.html', {})


def contact_view(request, *args, **kwargs):
    return render(request, 'sargam/contact.html', {})
