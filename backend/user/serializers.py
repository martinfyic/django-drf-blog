from rest_framework.serializers import ModelSerializer
from .models import User


class BlogSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
