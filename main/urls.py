from django.urls import path
from . import views
from .views import ProductListView, ProductHTMXView, create_product, edit_product, delete_product, validate_product_api

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('profile/<str:username>/', views.profile, name='profile'),  # URL dengan parameter
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_view, name='success_page'),
    path('massage/', views.masages_view, name='massage'),
    path('massageview/', views.daftar_pesan, name='daftar_pesan'),
    path('htmxtest/', views.htmx_view, name='htmx_test'),
    path('comment/', views.comment_view, name='comment_view'),
    path('get-data/', views.get_data, name='get_data'),
    path('post-data/', views.post_data, name='post_data'),
    path('api/comments/', views.get_comments, name='get_comments'),
    path('api/comments/post/', views.post_comment, name='post_comment'),
    path('product/', ProductListView.as_view(), name='product-list'),
    path('htmx/', ProductHTMXView.as_view(), name='product-list-htmx'),
    path('create/', create_product, name='product-create'),
    path('<int:pk>/edit/', edit_product, name='product-edit'),
    path('<int:pk>/delete/', delete_product, name='product-delete'),
    path('api/validate/', validate_product_api, name='product-validate-api'),
]