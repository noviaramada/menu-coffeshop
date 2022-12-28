from multiprocessing import context
from re import template
from turtle import title
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .models import Menu, Promosi
from .forms import MenuForms


def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else:
        return False


@login_required
def dashboard(request):
    if request.user.groups.filter(name='Operator').exists():
        request.session['is_operator'] = 'operator'
    template_name = "back/dashboard.html"
    context = {
        'title' : 'dashboard',
    }
    return render(request, template_name, context)       

@login_required
def menu(request):
    template_name = "back/tabel_menu.html"
    menu = Menu.objects.all()
    context = {
        'title' : 'tabel menu',
         'menu' : menu,
    }
    return render(request, template_name, context)    

@login_required
def promosi(request):
    template_name = "back/tabel_promosi.html"
    promosi = Promosi.objects.all()
    context = {
        'title' : 'Promosi',
        'promosi' : promosi,
    }
    return render(request, template_name, context)

def users(request):
    template_name = "back/tabel_users.html"
    list_user = User.objects.all()
    context = {
        'title' : 'tabel user',
        'list_user' : list_user
    }
    return render(request, template_name, context)       

@login_required
def tambah_menu(request):
    template_name = "back/tambah_menu.html"
    if request.method == "POST":
        forms_menu = MenuForms(request.POST)
        if forms_menu.is_valid():
            forms_menu.save()


        return redirect(menu)
    else :
        forms_menu = MenuForms()
    context = {
        'title' : 'Tambah Menu',
        'forms_menu' :forms_menu
    }

    return render(request,template_name,context)        


@login_required
def tambah_promosi(request):
    template_name = "back/tambah_promosi.html"
    if request.method == "POST":
       nama = request.POST.get('nama')
       harga = request.POST.get('harga')
       deskripsi = request.POST.get('deskripsi')
       stok = request.POST.get('stok')
       Promosi.objects.create (
           nama = nama,
           harga = harga,
           deskripsi = deskripsi,
           stok = stok,
       )
       return redirect(promosi)
    context = {
        'title' : 'tambah promosi',
    }
    return render(request, template_name, context)  

@login_required
def lihat_menu(request, id):
    template_name = "back/lihat_menu.html"
    menu = Menu.objects.get(id=id)
    context = {
        'title' : 'Lihat Menu',
        'menu' : menu
    }
    return render(request, template_name, context)       

@login_required
def delete_menu(request, id):
    Menu.objects.get(id=id).delete()
    return redirect(menu)   

@login_required
def delete_promosi(request, id):
    Promosi.objects.get(id=id).delete()
    return redirect(promosi)   

@login_required
def edit_menu(request, id):
    template_name = "back/edit_menu.html"
    a = Menu.objects.get(id=id)
    if request.method == "POST":
        nama = request.POST.get("nama")
        harga = request.POST.get("harga")
        deskripsi = request.POST.get("deskripsi")
        stok = request.POST.get("stok")

        a.nama = nama
        a.harga = harga
        a.deskripsi = deskripsi
        a.stok = stok
        a.save()
        return redirect(menu)
    context = {
        'title' : 'edit Menu',
        'menu' : menu
    }
    return render(request, template_name, context)     
     
@login_required
def edit_promosi(request, id):
    template_name = "back/edit_promosi.html"
    p = Promosi.objects.get(id=id)
    if request.method == "POST":
        nama = request.POST.get("nama")
        harga = request.POST.get("harga")
        deskripsi = request.POST.get("deskripsi")
        stok = request.POST.get("stok")

        p.nama = nama
        p.harga = harga
        p.deskripsi = deskripsi
        p.stok = stok
        p.save()
        return redirect(promosi)
    context = {
        'title' : 'edit promosi',
        'promosi' : promosi
    }
    return render(request, template_name, context)     