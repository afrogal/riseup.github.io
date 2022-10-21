from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth import authenticate ,logout
#from django.contrib.auth import login as dj_login
from django.contrib.auth.models import User
#from .models import UserProfile

# Create your views here.
def registerUser(request):
    context = {}
    return render(request,'htmlFiles/register.html', context)

