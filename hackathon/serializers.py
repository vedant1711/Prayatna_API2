# hackathon/serializers.py

from rest_framework import serializers
from .models import Team, ApiHitCount

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'team_name', 'team_members', 'access_key']

class ApiHitCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiHitCount
        fields = ['api_code']