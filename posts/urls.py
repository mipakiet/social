from django.urls import path

from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('posts/<int:post_id>/', views.post, name='post'),
    path('posts/add/', views.add_post, name='add_post'),
    path('posts/delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('posts/like_post/<int:post_id>/', views.like_post, name='like_post'),
]
