from django.urls import path
from . import views

urlpatterns = [
    path('get', views.getBlogs, name='get_blogs'),
    path('get/<slug>', views.getOneBlog, name='get_one_blog'),
    path('post', views.postBlog, name='post_blog'),
    path('put/<slug>', views.putBlog, name='put_blog'),
    path('delete/<slug>', views.deleteBlog, name='delete_blog'),
]
