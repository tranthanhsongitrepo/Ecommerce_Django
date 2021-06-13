from django.contrib import admin

# Register your models here.
from staff.models import *
from product.models import *
from order.models import *
from user.models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image_tag', 'status', 'type']


admin.site.register(Storage)
admin.site.register(Fullname)
admin.site.register(Address)
admin.site.register(Manufacturer)
admin.site.register(Item)
admin.site.register(ItemInCart)
admin.site.register(Cart)
admin.site.register(Order)
