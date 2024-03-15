from rest_framework import serializers
from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'username', 'name', 'team_members', 'api_code', 'time_refreshed']
