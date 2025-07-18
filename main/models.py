from django.db import models
from django.utils import timezone

# Create your models here.
class Pesan(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nama")
    email = models.EmailField(verbose_name="Email")
    isi = models.TextField(verbose_name="Pesan")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Waktu Kirim")

    def __str__(self):
        return f"Pesan dari {self.name}"

    class Meta:
        verbose_name_plural = "Pesan Masuk"
        ordering = ['-created_at']  # Urutkan terbaru pertama

class Comment(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Komentar oleh {self.name}"
    
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nama Produk")
    description = models.TextField(verbose_name="Deskripsi")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Harga")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Waktu Dibuat")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Produk"
        ordering = ['-created_at']  # Urutkan terbaru pertama   