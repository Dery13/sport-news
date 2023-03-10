from django.db import models

# Create your models here.

class Kategori(models.Model):
    nama = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural = "Kategori"

class Artikel(models.Model):
    nama = models.CharField(max_length=100, blank=True, null=True)
    judul = models.CharField(max_length=100)
    isi = models.CharField(max_length=100, blank=True,null=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{} . {}".format(self.nama, self.judul)
    
    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Artikel"
        
class Berita(models.Model):
    nama = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    desc = models.TextField(max_length=100, blank=True, null=True)
    tanggal = models.CharField(max_length=100)
    link = models.CharField(max_length=100, blank=True, null=True)
    conten = models.TextField(blank=True, null=True)
    img = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return "{} . {}".format(self.nama, self.title)
        