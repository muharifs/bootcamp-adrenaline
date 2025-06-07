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