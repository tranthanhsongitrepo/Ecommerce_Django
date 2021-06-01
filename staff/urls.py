from django.urls import path

from .views import list_staff, create_staff, get_products, create_product, update_product, delete_product

urlpatterns = [
    path('list_staff', list_staff, name='list_staff'),
    path('create_staff', create_staff, name='create_staff'),
    path('products', get_products, name='search_products'),
    path('products', get_products, name='search_products_by_name'),
    path('create_product', create_product, name='create_product'),
    path('delete_product/<int:product_id>', delete_product, name='delete_product'),
    path('update_product/<int:product_id>', update_product, name='update_product'),
]