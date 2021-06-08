from django.conf.urls.static import static
from django.urls import path

from djangoProject import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('view_cart', views.view_cart, name='view_cart'),
    path('delete_item/<int:id>', views.delete_item, name='delete_item'),
    path('order/order_item', views.order_item, name='order_item'),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)