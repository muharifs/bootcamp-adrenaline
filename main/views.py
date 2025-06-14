from django.shortcuts import redirect, render
from .forms import ContactForm
from .forms import PesanForm
from .models import Pesan
from .models import Comment
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json

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

def comment_view(request):
    return render(request, 'main/comment.html')

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

@require_http_methods(["GET"])
def get_comments(request):
    comments = Comment.objects.all().order_by('-created_at')
    comments_data = [
        {
            'name': comment.name,
            'content': comment.content,
            'created_at': comment.created_at.strftime("%d %b %Y %H:%M")
        }
        for comment in comments
    ]
    return JsonResponse({'comments': comments_data})


@require_http_methods(["POST"])
def post_comment(request):
    try:
        # Untuk form-data
        if request.content_type == 'application/x-www-form-urlencoded':
            name = request.POST.get('name')
            content = request.POST.get('content')
        # Untuk JSON
        else:
            data = json.loads(request.body)
            name = data.get('name')
            content = data.get('content')
        
        if not name or not content:
            return JsonResponse({'success': False, 'error': 'Nama dan konten diperlukan'}, status=400)
            
        comment = Comment.objects.create(
            name=name,
            content=content
        )
        return JsonResponse({
            'success': True,
            'comment': {
                'name': comment.name,
                'content': comment.content,
                'created_at': comment.created_at.strftime("%d %b %Y %H:%M")
            }
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)