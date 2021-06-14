from django.contrib import admin

# Register your models here.
from product.forms import ProductForm, ClothingForm
from product.models import Clothing, Book, Electronic, Item, Manufacturer


class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    search_fields = ['name']


class ClothingAdmin(ProductAdmin):
    form = ClothingForm


class BookAdmin(ProductAdmin):
    form = ClothingForm


class ElectronicAdmin(ProductAdmin):
    form = ClothingForm


admin.site.register(Clothing, ClothingAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Electronic, ElectronicAdmin)
admin.site.register(Item)
admin.site.register(Manufacturer)
