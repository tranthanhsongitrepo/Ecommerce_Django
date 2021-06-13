from django.urls import path

from user.views import login_view, register_view, logout_view

urlpatterns = [
    path('user/login', login_view, name="login"),
    path('user/register', register_view, name="register"),
    path('user/logout', logout_view, name="logout"),
]
