from django import forms
from PIL import ImageFilter
from product.models import Items

class ItemForm(forms.ModelForm):
    class Meta:
        model = Items

        fields = [
            'name',
            'img',
            'detail',
            'price',
            'quantity'
        ]
        
        lables = {

            'name':'Name of the product',
            'img': 'photo of the product',
            'detail':'Description of the product',
            'price':'Price of the product',
            'quantity': 'How many do you have available?'
        }

        # widgets = {
        #     'name':forms.TextInput(attrs={'class':'form-control'}),
        #     'detail':forms.Textarea(attrs={'class':'form-control'}),
        #     'price':forms.TextInput(attrs={'class':'form-control'}),
        #     'quantity': forms.TextInput(attrs={'class':'form-control'}),

        # }