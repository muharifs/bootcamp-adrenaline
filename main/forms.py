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

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nama Produk',
                'hx-post': '/products/api/validate/',
                'hx-trigger': 'keyup changed delay:500ms',
                'hx-target': '#name-errors',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Deskripsi Produk',
                'rows': 3
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Harga',
                'hx-post': '/products/api/validate/',
                'hx-trigger': 'keyup changed delay:500ms',
                'hx-target': '#price-errors',
            }),
        }