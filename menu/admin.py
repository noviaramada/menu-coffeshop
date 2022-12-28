from django.contrib import admin

from .models import *
# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    list_display = ['nama','harga','deskripsi','stok']

admin.site.register(Menu, MenuAdmin)

class PromosiAdmin(admin.ModelAdmin):
    list_display = ['nama','harga','deskripsi','stok']

admin.site.register(Promosi, PromosiAdmin)