from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import *
from .forms import SessionForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.conf import settings

import requests
from urllib.parse import quote

# Create your views here.

def index(request):
    return render(request, 'proj_app/index.html')

def listings(request):
    sessions = Session.objects.all()
    print("public sessions", sessions)
    return render(request, 'proj_app/listings.html', {'sessions': sessions})

def sessionDetails(request, pk):
    session = get_object_or_404(Session, pk=pk)
    return render(request, 'proj_app/session_details.html', {'session': session})

@login_required
def sessionUpdate(request, pk):
    session = get_object_or_404(Session, pk=pk)
    if request.method == 'POST':
        form = SessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('sessionDetails', pk)
    else:
        form = SessionForm(instance=session)
    context = {'form': form}
    return render(request, 'proj_app/session_form.html', context)

@login_required
def sessionDelete(request, pk):
    session = get_object_or_404(Session, pk=pk)
    if request.method == 'POST':
        session.delete()
        return redirect('listings')
    context = {'session': session}
    return render(request, 'proj_app/session_delete.html', context)

@login_required
def sessionCreate(request):
    if request.method == 'POST':
        if 'selected_game' in request.POST:
            game_id = request.POST['selected_game']
            encoded_id = quote(game_id)
            encoded_key = quote(settings.MOBY_KEY, safe='')
            api_url= f'https://api.mobygames.com/v1/games/{encoded_id}?api_key={encoded_key}'
            response = requests.get(api_url)
            if response.status_code == 200:
                form = SessionForm()
                game = response.json()
                form.fields['game_name'].initial = game['title']
                form.fields['thumbnail'].initial = game['sample_cover']['thumbnail_image']
                return render(request, 'proj_app/session_form.html', {'form': form})
            else:
                error_message = f'Error: {response.status_code} - {response.text}'
                return render(request, 'proj_app/session_form.html', {'form': form, 'error_message': error_message})
        else:
            form = SessionForm(request.POST)
            if form.is_valid():
                session = form.save(commit=False)
                session.owner = request.user
                session.save()
                return redirect('listings')
            else:
                print(form.errors)
    if request.method == 'GET' and 'game_name' in request.GET:
        game_name = request.GET['game_name']
        encoded_id = quote(game_name)
        encoded_key = quote(settings.MOBY_KEY, safe='')
        api_url= f'https://api.mobygames.com/v1/games?api_key={encoded_key}&title={encoded_id}'
        response = requests.get(api_url)
        if response.status_code == 200:
            form = SessionForm()
            games = response.json()
            return render(request, 'proj_app/session_form.html', {'form': form, 'games' : games['games']})
        else:
            error_message = f'Error: {response.status_code} - {response.text}'
            return render(request, 'proj_app/session_form.html', {'form': form, 'error_message': error_message})
    else:
        form = SessionForm()
    return render(request, 'proj_app/session_form.html', {'form': form})

@login_required
def userLogout(request):
    logout(request)
    return render(request, 'registration/logged_out.html')

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='Players')
            user.groups.add(group)
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'registration/register.html', context)
