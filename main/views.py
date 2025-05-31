from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
     return render(request, 'main/index.html')

def about(request):
    context = {
        'title': 'Tentang Kami',
        'message': 'Ini adalah halaman about.'
    }
    return render(request, 'main/about.html', context)

def profile(request, username):
    # Mengambil username dari parameter URL
    usernameFormat = username.title() if username else 'Anonymous'
    context = {
        'username': usernameFormat,
        'judul': 'Halaman Profile'
    }
    return render(request, 'main/profile.html', context)