from django import forms
from .models import *

class ContactForm(forms.Form):
    nama = forms.CharField(
        label='Nama Lengkap',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Alamat Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    pesan = forms.CharField(
        label='Pesan Anda',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    )

class PesanForm(forms.ModelForm):
    class Meta:
        model = Pesan
        fields = ['name', 'email', 'isi']