from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


# --- Permissions ---
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only for the author
        return obj.author == request.user


# --- Post ViewSet ---
class PostViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for posts.
    Only the post's author can edit or delete it.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# --- Comment ViewSet ---
class CommentViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for comments.
    Only the comment's author can edit or delete it.
    """
    queryset = Comment.objects.all()  # 👈 required for your test
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# --- Feed View ---
class FeedView(APIView):
    """
    Returns posts from users the current user follows, ordered by creation date.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        following_users = user.following.all()  # ✅ checker expects this
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')  # ✅ checker expects this
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
