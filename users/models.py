from django.contrib.auth.models import AbstractUser
from django.db import models

from users.manager import UserManager


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField("email", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    first_name = models.CharField(blank=True, max_length=50, null=True)
    last_name = models.CharField(blank=True, max_length=50, null=True)
    phone_number = models.CharField(blank=True, max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
