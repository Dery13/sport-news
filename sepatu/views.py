from blog.models import Artikel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.db import  transaction
from django.contrib.auth.hashers import make_password

from blog.models import Artikel,Berita
from user.models import Biodata
import requests

def home(request):
    template_name = 'front/home.html'
    artikel = Artikel.objects.all()
    context = {
        'title':'home',
        'artikel':artikel,
    }
    return render(request, template_name, context)
def base(request):
    template_name = 'front/base.html'
    context = {
        'title':'Tabel',
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'front/about.html'
    context = {
        'title':'about',
    }
    return render(request, template_name, context)

def artikel(request):
    template_name = 'front/artikel.html'
    artikel = Artikel.objects.all()
    context = {
        'title':'artikel',
        'artikel': artikel,
    }
    return render(request, template_name, context)

# def blog(request):
#     template_name = 'front/blog.html'
#     artikel = Artikel.objects.all()
#     context = {
#         'title':'blog',
#         'artikel':artikel
#     }
#     return render(request, template_name, context)

def berita(request):
    template_name = 'front/berita.html'
    berita = Berita.objects.all()
    context = {
        'title':'home',
        'berita':berita,
    }
    return render(request, template_name, context)

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    template_name = 'account/login.html'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None :
            pass
            print("username benar" )
            auth_login(request, user)
            return redirect('home')
        else:
            pass
            print("username salah" )
    context = {
        'title':'form',
    }
    return render(request, template_name, context)
def logout_view(request):
    logout(request)
    return redirect('home')

def register(request):
    template_name = 'account/register.html'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        nama_depan = request.POST.get('nama_depan')
        nama_belakang = request.POST.get('nama_belakang')
        email = request.POST.get('email')
        alamat = request.POST.get('alamat')
        telp = request.POST.get('telp')

        try:
            with transaction.atomic():
                User.objects.create(
                    username = username,
                    password = make_password(password),
                    first_name = nama_depan,
                    last_name= nama_belakang,
                    email = email
                )
                get_user = User.objects.get(username = username)
                Biodata.objects.create(
                    user = get_user,
                    alamat = alamat,
                    telp = telp,
                )
            return redirect(home)
        except:pass
        print(username,password,nama_depan,nama_belakang,email,alamat,telp)
    context = {
        'title':'form register',
    }
    return render(request, template_name, context)