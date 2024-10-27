from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Comment
from .serializers import CommentSerializer
from mbp_blog_app.models import BlogPost
from django.shortcuts import get_object_or_404
from django.http import Http404


class CommentViewSet(ViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    # Show all the comments
    def list(self, request):
        try:
            comments = Comment.objects.all()
            serializer = CommentSerializer(comments, many=True)
            
            if(serializer.data):
                return Response(
                    {
                        "message": "All comments are retrived successfully",
                        "status": status.HTTP_200_OK,
                        "data": serializer.data
                    }
                )
            else:
                return Response(
                    {
                        "message": "No comment found",
                        "status": status.HTTP_200_OK,
                        "data": serializer.data
                    }
                )

        except Exception as e:
            return Response(
                {
                    "message": "Something went wrong",
                    "error": str(e),
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR
                }, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
0