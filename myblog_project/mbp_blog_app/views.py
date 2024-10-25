from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            
            return Response(
                {
                    "message": "Blog posts retrieved successfully!",
                    "status_code": status.HTTP_200_OK,
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    "message": "Error retrieving blog posts.",
                    "error": str(e),
                    "status_code": status.HTTP_400_BAD_REQUEST
                },
                status=status.HTTP_400_BAD_REQUEST
            )
            
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            
            # Save with the currently logged-in user as the author
            serializer.save(author=request.user)
            
            return Response(
                {
                    "message": "Blog post created successfully!",
                    "status_code": status.HTTP_201_CREATED,
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {
                    "message": "Error creating blog post.",
                    "error": str(e),
                    "status_code": status.HTTP_400_BAD_REQUEST
                },
                status=status.HTTP_400_BAD_REQUEST
            )
            
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(
                {
                    "message": "Blog post retrieved successfully!",
                    "status_code": status.HTTP_200_OK,
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )
        except Http404:
            return Response(
                {
                    "message": "Blog post not found.",
                    "status_code": status.HTTP_404_NOT_FOUND
                },
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {
                    "message": "Error retrieving blog post.",
                    "error": str(e),
                    "status_code": status.HTTP_400_BAD_REQUEST
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(
                {
                    "message": "Blog post updated successfully!",
                    "status_code": status.HTTP_200_OK,
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )
        except Http404:
            return Response(
                {
                    "message": "Blog post not found.",
                    "status_code": status.HTTP_404_NOT_FOUND
                },
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {
                    "message": "Error updating blog post.",
                    "error": str(e),
                    "status_code": status.HTTP_400_BAD_REQUEST
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(
                {
                    "message": "Blog post deleted successfully!",
                    "status_code": status.HTTP_204_NO_CONTENT
                },
                status=status.HTTP_204_NO_CONTENT
            )
        except Http404:
            return Response(
                {
                    "message": "Blog post not found.",
                    "status_code": status.HTTP_404_NOT_FOUND
                },
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {
                    "message": "Error deleting blog post.",
                    "error": str(e),
                    "status_code": status.HTTP_400_BAD_REQUEST
                },
                status=status.HTTP_400_BAD_REQUEST
            )