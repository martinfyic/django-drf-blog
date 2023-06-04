from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Blog
from .serializers import BlogSerializer


@api_view(['GET'])
def getBlogs(request):
    blog = Blog.objects.all()
    serializer = BlogSerializer(blog, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getOneBlog(request, slug):
    blog = Blog.objects.get(slug=slug)
    serializer = BlogSerializer(blog, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def postBlog(request):
    data = request.data
    blog = Blog.objects.create(
        title=data['title'],
        overview=data['overview'],
        content=data['content'],
        feature=data['feature'],
    )
    categories = data.get('categories', [])
    blog.categories.set(categories)
    serializer = BlogSerializer(blog, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def putBlog(request, slug):
    data = request.data
    blog = Blog.objects.get(slug=slug)
    serializer = BlogSerializer(instance=blog, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@api_view(['DELETE'])
def deleteBlog(request, slug):
    blog = Blog.objects.get(slug=slug)
    blog.delete()
    return Response('Blog Eliminado')
