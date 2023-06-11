from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Blog
from .serializers import BlogSerializer


class BlogPagination(PageNumberPagination):
    page_size = 10  # Número de elementos por página
    # Parámetro opcional para cambiar el número de elementos por página
    page_size_query_param = 'page_size'
    max_page_size = 100  # Número máximo de elementos por página permitido

    # Opcional: puedes personalizar la respuesta de paginación
    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'results': data
        })


@swagger_auto_schema(
    method='get',
    operation_description="Obtener todos los blogs.",
    tags=['Blogs'],
)
@api_view(['GET'])
def getBlogs(request):
    """
    Vista para obtener todos los blogs.
    """
    blog = Blog.objects.all()
    paginator = BlogPagination()
    paginated_blog = paginator.paginate_queryset(blog, request)
    serializer = BlogSerializer(paginated_blog, many=True)
    return paginator.get_paginated_response(serializer.data)


@swagger_auto_schema(
    method='get',
    operation_description="Obtener un blog por su slug.",
    tags=['Blogs'],
)
@api_view(['GET'])
def getOneBlog(request, slug):
    """
    Vista para obtener un blog por su slug.
    """
    blog = Blog.objects.get(slug=slug)
    serializer = BlogSerializer(blog, many=False)
    return Response(serializer.data)


@swagger_auto_schema(
    method='post',
    operation_description="Crear un nuevo blog.",
    tags=['Blogs'],
)
@api_view(['POST'])
def postBlog(request):
    """
    Vista para crear un nuevo blog.
    """
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


@swagger_auto_schema(
    method='put',
    operation_description="Actualizar un blog por su slug.",
    tags=['Blogs'],
)
@api_view(['PUT'])
def putBlog(request, slug):
    """
    Vista para actualizar un blog por su slug.
    """
    data = request.data
    blog = Blog.objects.get(slug=slug)
    serializer = BlogSerializer(instance=blog, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@swagger_auto_schema(
    method='delete',
    operation_description="Eliminar un blog por su slug.",
    tags=['Blogs'],
)
@api_view(['DELETE'])
def deleteBlog(request, slug):
    """
    Vista para eliminar un blog por su slug.
    """
    blog = Blog.objects.get(slug=slug)
    blog.delete()
    return Response('Blog Eliminado')
