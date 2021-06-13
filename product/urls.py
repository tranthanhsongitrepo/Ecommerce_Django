from django.urls import path

from product.views import detailProduct, add_to_cart, shoppingCart, order_item, home, search_items

urlpatterns = [
    path('', home, name='home'),
    path('product-details/<int:product_id>', detailProduct, name='product-details'),
    path('add-to-cart/<int:id>', add_to_cart, name='add-to-cart'),
    path('shopping-cart', shoppingCart, name='shopping-cart'),
    path('check-out', order_item, name='check-out'),
    path('search-products', search_items, name='search-products'),
]