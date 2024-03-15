# hackathon/models.py

from django.db import models
import uuid
from django.utils import timezone

class Team(models.Model):
    team_name = models.CharField(max_length=255)
    team_members = models.TextField()
    access_key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)


class ApiHitCount(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    api_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    time_refreshed = models.DateTimeField(default=timezone.now)
    api_hits = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)