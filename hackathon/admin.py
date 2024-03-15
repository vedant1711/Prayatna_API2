from django.contrib import admin
from .models import Team, ApiHitCount

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'access_key')

@admin.register(ApiHitCount)
class ApiHitCountAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'api_code', 'time_refreshed', 'api_hits', 'timestamp')

    def team_name(self, obj):
        return obj.team.team_name

    team_name.admin_order_field = 'team__team_name'