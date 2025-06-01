from django.shortcuts import redirect, render
from .forms import ContactForm

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

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Proses data disini (contoh simpan ke database atau kirim email)
            nama = form.cleaned_data['nama']
            email = form.cleaned_data['email']
            pesan = form.cleaned_data['pesan']
            
            # Redirect setelah sukses
            return redirect('success_page')
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})

def success_view(request):
    return render(request, 'main/success.html')