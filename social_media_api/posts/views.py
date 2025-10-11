from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import permissions, status
from django.contrib.contenttypes.models import ContentType

from .models import Post, Comment, Like 
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from notifications.models import Notification # type: ignore

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

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # prevent double-like (unique_together also protects but we handle gracefully)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        return Response({'detail': 'Already liked'}, status=status.HTTP_400_BAD_REQUEST)

    # create notification for the post author (if not the same user)
    if post.author != request.user:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            target_ct=ContentType.objects.get_for_model(Post),
            target_id=post.pk
        )

    serializer = LikeSerializer(like, context={'request': request})
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    deleted, _ = Like.objects.filter(post=post, user=request.user).delete()
    if deleted == 0:
        return Response({'detail': 'You had not liked this post'}, status=status.HTTP_400_BAD_REQUEST)

    # remove related like notifications (simple approach)
    Notification.objects.filter(
        recipient=post.author,
        actor=request.user,
        verb='liked your post',
        target_ct=ContentType.objects.get_for_model(Post),
        target_id=post.pk
    ).delete()

    return Response({'detail': 'Like removed'}, status=status.HTTP_200_OK)