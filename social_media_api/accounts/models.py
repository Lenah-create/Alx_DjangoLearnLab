from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Custom user model extending AbstractUser.
    Fields:
      - username, password, email, first_name, last_name (from AbstractUser)
      - bio: short bio text
      - profile_picture: optional image (requires MEDIA settings + media serving)
      - followers: many-to-many to self (asymmetric)
    """
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    # followers: users who follow this user
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following',
        blank=True
    )

    def __str__(self):
        return self.username
