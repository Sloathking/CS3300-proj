from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import SessionForm

# Create your views here.

def index(request):
    return render(request, 'proj_app/index.html')

def listings(request):
    public_sessions = Session.objects.filter(is_public=True)
    print("public sessions", public_sessions)
    return render(request, 'proj_app/listings.html', {'public_sessions': public_sessions})

def sessionDetails(request, pk):
    session = get_object_or_404(Session, pk=pk)
    return render(request, 'proj_app/session_details.html', {'session': session})

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
