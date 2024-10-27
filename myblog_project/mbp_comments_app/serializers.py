from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  
    class Meta:
        model = Comment
        fields = ['id', 'blog_post', 'user', 'content', 'created_at']
