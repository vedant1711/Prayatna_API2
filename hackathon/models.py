# hackathon/models.py

from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class Team(AbstractUser):
    username = None
    team_name = models.CharField(unique=True, max_length=16)
    # Add other relevant fields
    team_members = models.TextField()
    access_key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    api_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    time_refreshed = models.DateTimeField(default=timezone.now)
    api_hits = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    
    REQUIRED_FIELDS = []

