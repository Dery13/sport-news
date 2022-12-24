from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Kategori)

class ArtikelAdmin(admin.ModelAdmin):
    list_display = ('nama','judul','isi','kategori','date')


admin.site.register(Artikel, ArtikelAdmin)

class BeritaAdmin(admin.ModelAdmin):
     list_display = ('nama','title','desc','tanggal','link','conten','img')
admin.site.register(Berita,BeritaAdmin)
    
    
