from django.contrib import admin

# Register your models here.
from staff.models import StorageStaff, Storage, Fullname, Address, Product, Manufacturer, Item, ItemInCart, Cart, \
    ProductImage


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Storage)
admin.site.register(Fullname)
admin.site.register(Address)
admin.site.register(StorageStaff)
admin.site.register(Product, ProductAdmin)
admin.site.register(Manufacturer)
admin.site.register(Item)
admin.site.register(ItemInCart)
admin.site.register(Cart)
admin.site.register(ProductImage)
