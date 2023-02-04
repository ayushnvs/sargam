from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
import os

verifiedUsers = ['ayushvns', 'akanksha', 'ayushm']

available_songs = os.listdir('./static/Songs')
def get_song_dict(available_songs):
    Dict = []
    for songs in available_songs:
        song_path = f'/static/Songs/{songs}'
        # print('.' in songs)
        song_name = songs.split('.')[0]
        Dict.append({'name': song_name, 'path': song_path})
    return Dict

# print(get_song_dict(available_songs))


def login_view(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(f'/{username}')
        else:
            messages.success(request,
                             ('There was an error... Please try again.'))
            return render(request, 'auth/login.html', {})
    else:
        if request.user.is_authenticated:
            return redirect(f'/{request.user.username}')
        return render(request, 'auth/login.html', {})


def loggedin_view(request, username):
    if username == request.user.username:
        return render(request, 'user/home.html', {
            "username": request.user.username,
            'verifiedUsers': verifiedUsers,
            'musicData': get_song_dict(available_songs)
        })
    return redirect('log_in')


def logout_view(request):
    logout(request)
    messages.success(request, ('You have been logged out!'))
    return redirect('log_in')


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print('Is form valid: ', form.is_valid())
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            # messages.success(request, ('Registraction Successful!'))
            return redirect(f'/{request.user.username}')
    else:
        if request.user.is_authenticated:
            return redirect(f'/{request.user.username}')
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})
