from rest_framework.serializers import ModelSerializer
from .models import Blog, Category


class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
