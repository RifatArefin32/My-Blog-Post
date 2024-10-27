from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet

router = DefaultRouter()
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('comments/blog_post/<int:id>', CommentViewSet.as_view({'get': 'comments_of_a_blog_post'}), name='comments-of-a-blog-post'),
    path('comments/blog_post/<int:id>/update/<int:comment_id>', CommentViewSet.as_view({'put': 'update_comment'}), name='update-comment'),
]
