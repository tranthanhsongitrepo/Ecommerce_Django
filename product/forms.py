from django import forms

from product.models import Product, Clothing


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['type']


class ClothingForm(ProductForm):
    class Meta:
        model = Clothing
        exclude = ['type']


class BookForm(ProductForm):
    class Meta:
        model = Clothing
        exclude = ['type']


class ElectronicForm(ProductForm):
    class Meta:
        model = Clothing
        exclude = ['type']
