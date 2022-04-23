from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.contrib import messages

import requests
import json



# Create your views here.
def home_view(request):
    return render(request,"incupad_app/home.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        User = auth.authenticate(password=password,username=username)
        if User is not None:
            login(request, User)
            return render(request,"incupad_app/choice.html")
        else:
            messages.info(request, 'invalid username or password')
            return HttpResponseRedirect('/login')
    return render(request, "incupad_app/login.html")

def logout_view(request):
    logout(request)
    messages.warning(request,"logout successfully!!")
    return HttpResponseRedirect('/login')

def choice_view(request):
    return render(request, "incupad_app/choice.html")

def register_view(request):

    url = "http://54.218.24.123/api/v1/master/masjidlist/"

    payload = json.dumps({
      "keyword": ""
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    context = {
        "data": json.loads(response.text)['list']
    }

    
    return render(request, "incupad_app/registration.html", context)





def update_view(request):
    return render(request, "incupad_app/update.html")