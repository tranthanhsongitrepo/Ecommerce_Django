from django.urls import path

from .views import list_staff

urlpatterns = [
    path('', list_staff, name='list_staff')
]