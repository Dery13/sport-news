from django.shortcuts import render,redirect
from multiprocessing import context
from .models import Artikel, Kategori,Berita
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
import requests

def is_creator(user):
    if user.groups.filter(name='Creator').exists():
        return True
    else:
        return False

@login_required
def dashboard(request):
    if request.user.groups.filter(name='Creator').exists():
        request.session['is_creator'] = 'creator'
    
    template_name = "back/dashboard.html"
    context = {
        'title' : 'dashboard',
    } 
    return render(request, template_name, context)

@login_required
@user_passes_test(is_creator)
def artikel(request):
    template_name = "back/tabel_artikel.html"
    artikel = Artikel.objects.all()
    # print(artikel)
    context = {
        'title' : 'dashboard',
        'artikel': artikel,
    }
    return render(request, template_name, context)

def berita(request):
    template_name = "back/tabel_berita.html"
    berita = Berita.objects.all()
    # print(artikel)
    context = {
        'title' : 'dashboard',
        'berita': berita,
    }
    return render(request, template_name, context)


@login_required
@user_passes_test(is_creator)
def users(request):
    template_name = "back/tabel_users.html"
    list_user = User.objects.all()
    context = {
        'title' : 'tabel_user',
        'list_user' : list_user
    }
    return render(request, template_name, context)

# @login_required
def tambah_artikel(request):
    template_name = "back/tambah_artikel.html"
    kategori = Kategori.objects.all()
    if request.method == "POST":
        kategori = request.POST.get('kategori')
        nama = request.POST.get('nama')
        judul = request.POST.get('judul')
        isi = request.POST.get('isi')
        kat = Kategori.objects.get(nama=kategori)
      
        #simpan produk karena ada relasi ke tabel kategori 
        Artikel.objects.create(
            nama = nama,
            judul = judul,
            isi = isi,
            kategori = kat,
        )
        return redirect (artikel)
    context = {
        'title':'Tambah Artikel',
        'kategori':kategori,
    }
    return render(request, template_name, context)

# @login_required
def lihat_artikel(request, id):
    template_name = "back/lihat_artikel.html"
    artikel = Artikel.objects.get(id=id)
    context = {
        'title' : 'View Artikel',
        'artikel' :artikel,
    }
    return render(request, template_name, context)

# @login_required
def edit_artikel(request ,id ):
    template_name = 'back/edit_artikel.html'
    kategori = Kategori.objects.all()
    a = Artikel.objects.get(id=id)
    if request.method == "POST":
        
        kategori = request.POST.get('kategori')
        nama = request.POST.get('nama')
        judul = request.POST.get('judul')
        isi = request.POST.get('isi')
        kat = Kategori.objects.get(nama=kategori)

        #input Kategori Dulu
        

        #simpan produk karena ada relasi ke tabel kategori 
        a.nama = nama
        a.judul = judul
        a.isi = isi
        a.kategori = kat
        a.save() 
        return redirect(artikel)
    context = {
        'title':'Edit Artikel',
        'kategori':kategori,
        'artikel' : artikel,

    }
    return render(request, template_name, context)

# @login_required
def hapus_artikel(request,id):
    Artikel.objects.get(id=id).delete()
    return redirect(artikel)

def sinkron_berita(request):
	url = "https://newsapi.org/v2/top-headlines?country=id&category=sports&apiKey=cf90c64250eb4cb2b85dcae943394920"
	data = requests.get(url).json()
	for d in data['articles']:
		cek_berita = Berita.objects.filter(nama=d['author'])
		if cek_berita:
			print('data sudah ada')
			c = cek_berita.first()
			c.nama=d['author']
			c.save()
		else: 
      		#jika belum ada maka tulis baru kedatabase
			b = Berita.objects.create(
				nama = d['author'],
				title = d['title'],
				desc = d['description'],
				tanggal = d['publishedAt'],
				link = d['url'],
                conten = d['content'],
				img = d['urlToImage'],
			)
	return redirect(berita)
def hapus_berita(request,id):
    Berita.objects.get(id=id).delete()
    return redirect(berita)

