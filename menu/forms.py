
from django import forms
from .models import Menu

class MenuForms(forms.ModelForm):
    class Meta :
        model = Menu
        fields = ('nama', 'deskripsi', 'harga', 'stok', 'menu_image')
        widgets = {
            "nama" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type' : 'text',
                    'placeholder' : "nama minuman",
                    'Required' :True
                }),  

            "deskripsi" : forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder' : "deskripsi",
                    'cols' : '30',
                    'rows' : '5',
                    'Required' :True
                }),  

            "harga" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type' : 'int',
                    'placeholder' : "harga",
                    'Required' :True
                }),  

            "stok" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type' : 'int',
                    'placeholder' : "stok",
                    'Required' :True
                }),                
        }
