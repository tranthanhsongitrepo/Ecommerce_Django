from django.contrib import admin

# Register your models here.
from staff.models import StorageStaff, Storage, Fullname, Address, Product, Manufacturer

admin.site.register(Storage)
admin.site.register(Fullname)
admin.site.register(Address)
admin.site.register(StorageStaff)
admin.site.register(Product)
admin.site.register(Manufacturer)
