from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from kasir.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('menu.urls')),
    path('',index, name='index'),
    path('users/',getUser, name='users'),
    path('about',about, name='about'),
    # path('berita',berita, name='berita'),
    path('login/', login, name='login'),
    path('logout/',logout_view, name='logout'),
    path('registrasi/',registrasi, name='registrasi'),
    path('menu/', include('menu.urls')),
    path('menu_list',menu_list, name='menu_list'),
    path('promosi_list',promosi_list, name='promosi_list'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
