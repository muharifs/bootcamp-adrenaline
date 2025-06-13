from django.shortcuts import redirect, render
from .forms import ContactForm
from .forms import PesanForm
from .models import Pesan

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

def masages_view(request):
    if request.method == 'POST':
        form = PesanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daftar_pesan')  # Ganti dengan URL tujuan setelah submit
    else:
        form = PesanForm()
    
    return render(request, 'main/massage.html', {'form': form})

def daftar_pesan(request):
    semua_pesan = Pesan.objects.all()
    return render(request, 'main/massage_view.html', {'pesan_list': semua_pesan})

def htmx_view(request):
    return render(request, 'main/htmx.html')

def get_data(request):
    # Data dari database atau lainnya
    items = ["Item 1", "Item 2", "Item 3"]
    return render(request, 'main/partial.html', {'items': items})

def post_data(request):
    if request.method == 'POST':
        # Proses data POST
        received_data = request.POST.get('data')
        return HttpResponse(f"Data diterima: {received_data}")
    return HttpResponse("Metode tidak diizinkan", status=405)
