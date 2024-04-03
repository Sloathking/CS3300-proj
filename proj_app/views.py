from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'proj_app/index.html')

def listings(request):
    public_sessions = Session.objects.filter(is_public=True)
    print("public sessions", public_sessions)
    return render(request, 'proj_app/listings.html', {'public_sessions': public_sessions})