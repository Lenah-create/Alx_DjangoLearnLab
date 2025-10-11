from django.urls import path
from .views import RegisterView, LoginView, ProfileView
from rest_framework.authtoken import views as drf_views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),            # custom login returns token
    path('profile/', ProfileView.as_view(), name='profile'),
    # optional: token auth obtain endpoint (DRF)
    path('token-auth/', drf_views.obtain_auth_token, name='token-auth'),
]
