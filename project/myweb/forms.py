from . models import product
from django import forms
from django.contrib.auth.forms import UserCreationForm

class ProductForm(forms.ModelForm):
    class Meta:
        model=product
        fields=('product_name','product_price','product_quantity')







