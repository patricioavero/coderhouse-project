from django.shortcuts import render
from .models import member

# Create your views here.

def home(request):
    return render(request, 'home.html')

def members(request):
    r_members_list = member.objects.all()
    return render(request, 'members.html', {"members": r_members_list})