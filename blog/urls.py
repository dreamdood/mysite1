from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/post/<int:post_id>', views.post_id, name='post_id'),
    path('', views.user, name='profile'),
]