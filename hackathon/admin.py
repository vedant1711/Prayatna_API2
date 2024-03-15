from django.contrib import admin
from .models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'access_key')

# @admin.register(ApiHitCount)
# class ApiHitCountAdmin(admin.ModelAdmin):
#     list_display = ('team', 'api_code', 'time_refreshed', 'api_hits', 'timestamp')