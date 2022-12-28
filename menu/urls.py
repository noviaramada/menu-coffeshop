from re import template
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('menu/', menu, name='tabel_menu'),
    path('users/', users, name='tabel_users'),
    path('promosi/', promosi, name='tabel_promosi'),
    path('tambah_menu/', tambah_menu, name='tambah_menu'),
    path('tambah_promosi/', tambah_promosi, name='tambah_promosi'),
    path('lihat_menu/<str:id>', lihat_menu, name='lihat_menu'),
    path('edit_menu/<str:id>', edit_menu, name='edit_menu'),
    path('edit_promosi/<str:id>', edit_promosi, name='edit_promosi'),
    path('delete_menu/<str:id>', delete_menu, name='delete_menu'),
    path('delete_promosi/<str:id>', delete_promosi, name='delete_promosi'),
]
