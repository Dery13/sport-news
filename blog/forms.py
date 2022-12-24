# from django import forms
# from .models import Artikel

# class JadwalForms(forms.ModelForm):
#     class Meta :
#         model = Artikel
#         fields = ('nama','jadwal','kategori','waktu','tanggal')
#         widget = {
#             "nama" : forms.textInput(
#                 attrs={
#                     'class': 'form-control',
#                     'type': 'text',
#                     'placeholder': "Nama",
#                     'required' : True,               
#            }),
#             "jadwal" : forms.textInput(
#                 attrs={
#                     'class': 'form-control',
#                     'type': 'text',
#                     'placeholder': "Subuh..Zuhur...Ashar...Maghrib...Isya",
#                     'required' : True,               
#            }),
#             "kategori" : forms.Select(
#                 attrs={
#                     'class': 'form-control',
#                     'type' : 'text',
#                     'col-md-3' : 'control-label',
#                     'required' : True,               
#            }),
#             "waktu" : forms.textInput(
#                 attrs={
#                     'class': 'form-control',
#                     'col-md-3' : 'control-label',
#                     'required' : True,               
#            }),
#             "tanggal" : forms.textInput(
#                 attrs={
#                     'class': 'form-control',
#                     'type': 'text',
#                     'placeholder': '...',
#                     'required' : True,               
#            }),
            
#         }