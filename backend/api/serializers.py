from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Blog, Category


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class BlogSerializer(ModelSerializer):
    author = serializers.StringRelatedField()
    categories = CategorySerializer(many=True)

    class Meta:
        model = Blog
        fields = '__all__'
