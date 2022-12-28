from tokenize import blank_re
from django.db import models


class Menu(models.Model):
    nama = models.CharField(max_length=30)
    harga = models.IntegerField()
    deskripsi = models.TextField()
    stok =models.IntegerField()
    menu_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return "{} - {}".format(self.nama, self.harga)

class Promosi(models.Model):
    nama = models.CharField(max_length=30)
    harga = models.IntegerField()
    deskripsi = models.TextField()
    stok =models.IntegerField()
   
    class Meta :
        verbose_name_plural : "Promosi"

    def __str__(self):
        return "{} - {}".format(self.nama, self.harga)

