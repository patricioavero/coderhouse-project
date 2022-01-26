from django.shortcuts import render
from .models import member

# Create your views here.

def home(request):
    r_members_list = member.objects.all()
    return render(request, 'home.html', {"members": r_members_list}) 