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
    path('htmx/', views.htmx_view, name='htmx_test'),
    path('comment/', views.comment_view, name='comment_view'),
    path('get-data/', views.get_data, name='get_data'),
    path('post-data/', views.post_data, name='post_data'),
    path('api/comments/', views.get_comments, name='get_comments'),
    path('api/comments/post/', views.post_comment, name='post_comment'),
]