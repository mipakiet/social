from django.urls import path

from . import views

urlpatterns = [
    path('users/register', views.register_request, name='register'),
    path('users/login', views.login_request, name='login'),
    path('users/logout', views.logout_request, name='logout'),
]
