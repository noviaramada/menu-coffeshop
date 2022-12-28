
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.http import HttpResponse
import requests

from menu.models import Menu, Promosi

def getUser(request): 
    
    # print(users)
    return render(request, "front/resep.html", {'users': users})
    pass

def index(request):
    template_name = "front/index.html"
    menu = Menu.objects.all()
    context = {
        'title' : 'index',
        'menu' : menu,
    }
    return render(request, template_name, context)

def about(request):
    template_name = "front/about.html"
    context = {
        'title' : 'about',
    }
    return render(request, template_name, context)

def menu_list(request):
    template_name = "front/menu_list.html"
    menu = Menu.objects.all()
    # response = requests.get('http://system.jamkridakaltim.co.id/api/users')
    # users = response.json()
    context = {
        'title' : 'list menu',
        'menu' : menu,
        # 'users': users
    }
    return render(request, template_name, context)

# def berita(request):
#     template_name = "front/berita.html"
#     # menu = Menu.objects.all()
#     response = requests.get('https://newsapi.org/v2/everything?q=tesla&from=2022-11-24&sortBy=publishedAt&apiKey=48d6f0479c4a482ea25b843f3aaf3998')
#     users = response.json()
#     context = {
#         'title' : 'list berita',
#         # 'menu' : menu,
#         'users': users
#     }
#     return render(request, template_name, context)

def promosi_list(request):
    template_name = "front/promosi_list.html"
    promosi = Promosi.objects.all()
    context = {
        'title' : 'list promosi',
        'promosi' : promosi,
    }
    return render(request, template_name, context)


def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    template_name = 'account/login.html'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None :
            pass
            print("username benar" )
            auth_login(request, user)
            return redirect('index')
        else:
            pass
            print("username salah" )
    context = {
        'title':'form',
    }
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('index')

def registrasi(request):
    template_name = "account/register.html"
    context = {
        'title' : 'registrasi',
    }
    return render(request, template_name, context)
