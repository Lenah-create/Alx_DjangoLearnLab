from django.urls import path
from .views import RegisterView, LoginView, ProfileView
from rest_framework.authtoken import views as drf_views
from .views import (
    RegisterView,
    LoginView,
    ProfileView,
    FollowUserView,
    UnfollowUserView,
    FollowersListView,
    FollowingListView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),            # custom login returns token
    path('profile/', ProfileView.as_view(), name='profile'),
    # optional: token auth obtain endpoint (DRF)
    path('token-auth/', drf_views.obtain_auth_token, name='token-auth'),

    # follow management
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
    path('<int:user_id>/followers/', FollowersListView.as_view(), name='user-followers'),
    path('<int:user_id>/following/', FollowingListView.as_view(), name='user-following'),
]
