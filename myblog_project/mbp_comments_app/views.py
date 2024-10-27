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
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        "message": "No comment found",
                        "status": status.HTTP_204_NO_CONTENT,
                        "data": serializer.data
                    },
                    status=status.HTTP_204_NO_CONTENT
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

    
    # Create a comment
    def create(self, request):
        try:
            blog_post_id = request.data.get('blog_post')
            blog_post = get_object_or_404(BlogPost, id=blog_post_id)
            serializer = CommentSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save(user=request.user, blog_post=blog_post)
                
                return Response(
                    {
                        "message": "Comment created successfully!",
                        "status": status.HTTP_200_OK,
                        "data": serializer.data
                    },
                    status=status.HTTP_200_OK
                )
            
            return Response(
                {
                    "message": "Invalid request to comment",
                    "error": serializer.errors,
                    "status": status.HTTP_400_BAD_REQUEST
                },
                status=status.HTTP_400_BAD_REQUEST
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


    # Retrieve comments for a specific blogpost
    def comments_of_a_blog_post(self, request, id=None):
        try:
            blog_post = get_object_or_404(BlogPost, id=id)
            comments = Comment.objects.filter(blog_post=blog_post)
            serializer = CommentSerializer(comments, many=True)
            
            if serializer.data:
                return Response(
                    {
                        "message": "Comments retrived for specific blogpost",
                        "status": status.HTTP_200_OK,
                        "data": serializer.data
                    },
                    status=status.HTTP_200_OK
                )
            return Response(
                {
                    {
                        "message": "No comment found",
                        "status": status.HTTP_204_NO_CONTENT,
                        "data": serializer.data
                    }
                },
                status=status.HTTP_204_NO_CONTENT
            )
        except Exception as e:
            return Response(
                {
                    "message": "Error retrieving blog posts.",
                    "error": str(e),
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
    
    # Update a specific comment on a blog post
    def update_comment(self, request, id=None, comment_id=None):
        try:
            blog_post = get_object_or_404(BlogPost, id=id)
            comment = get_object_or_404(Comment, id=comment_id, blog_post=blog_post)
            
            # Check if the logged-in user is the author of the comment
            if comment.user != request.user:
                return Response(
                    {
                        "message": "You are not authorized to update this comment.",
                        "error": "Unauthorized access",
                        "status": status.HTTP_403_FORBIDDEN
                    }
                )

            # Update the comment
            serializer = CommentSerializer(comment, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "message": "Comment updated successfully",
                        "status": status.HTTP_200_OK,
                        "data": serializer.data
                    },
                    status=status.HTTP_200_OK
                )

            return Response(
                {
                    "message": "Error updating the comment",
                    "status":status.HTTP_400_BAD_REQUEST,
                    "error": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {
                    "message": "Something went wrong.",
                    "error": str(e),
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )