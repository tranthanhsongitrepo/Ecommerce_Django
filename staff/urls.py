from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from .views import list_staff, get_products, delete_product

urlpatterns = [
    path('list_staff', list_staff, name='list_staff'),
    path('products', get_products, name='search_products'),
    path('products', get_products, name='search_products_by_name'),
]

urlpatterns += staticfiles_urlpatterns()