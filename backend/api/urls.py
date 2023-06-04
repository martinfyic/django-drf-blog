from django.urls import path
from . import views

urlpatterns = [
    path('get', views.getBlogs, name='get_blogs'),
    path('get/<int:pk>', views.getOneBlog, name='get_one_blog'),
    path('post', views.postBlog, name='post_blog'),
    path('put/<int:pk>', views.putBlog, name='put_blog'),
    path('delete/<int:pk>', views.deleteBlog, name='delete_blog'),
]
