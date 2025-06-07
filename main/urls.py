from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('profile/<str:username>/', views.profile, name='profile'),  # URL dengan parameter
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_view, name='success_page'),
    path('massage/', views.masages_view, name='massage'),
    path('massageview/', views.daftar_pesan, name='daftar_pesan'),
]