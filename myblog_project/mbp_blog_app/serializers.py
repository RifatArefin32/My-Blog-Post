from rest_framework import serializers
from .models import BlogPost
from mbp_authentication.serializers import UserSerializer

class BlogPostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'created_at']
