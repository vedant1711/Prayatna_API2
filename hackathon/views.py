# hackathon/views.py

from rest_framework import generics
from rest_framework.response import Response
from .models import Team
from .serializers import TeamSerializer
import uuid
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


class TeamRegistrationView(generics.CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def perform_create(self, serializer):
        # Customize the data to be saved before creating the Team instance
        team_name = self.request.data.get('team_name', '')
        team_members = self.request.data.get('team_members', [])
        
        # Generate a UUID for the access key
        access_key = uuid.uuid4()
        api_code = uuid.uuid4()
        time_refreshed = timezone.now()


        # Save the Team instance with the generated access key
        serializer.save(team_name=team_name, team_members=team_members, access_key=access_key, api_code=api_code, time_refreshed=time_refreshed)

        # Return the access key in the response
        return Response({'access_key': str(access_key), 'api_code': str(api_code)})


class TeamInfoView(generics.RetrieveAPIView):
    serializer_class = TeamSerializer

    def get_object(self):
        access_key = self.request.headers.get('Authorization', '').replace('Bearer ', '')

        if not access_key:
            # Return a meaningful response or raise an appropriate exception
            return Response({'error': 'Access key is required in the Authorization header.'}, status=400)

        try:
            return Team.objects.get(access_key=access_key)
        except Team.DoesNotExist:
            # Handle the case when the team with the provided access key doesn't exist
            return Response({'error': 'Team not found.'}, status=404)


# class ApiCodeView(generics.CreateAPIView):
#     serializer_class = ApiHitCountSerializer

#     def create(self, request, *args, **kwargs):
#         access_key = self.request.headers.get('Authorization', '').replace('Bearer ', '')

#         if not access_key:
#             return Response({'error': 'Access key is required in the Authorization header.'}, status=400)

#         team = get_object_or_404(Team, access_key=access_key)
#         api_hit_count, created = ApiHitCount.objects.get_or_create(team=team)

#         # Check if the ApiHitCount was just created or if it needs to be refreshed
#         if created or (timezone.now() - api_hit_count.time_refreshed).total_seconds() >= 1800:
#             api_hit_count.api_code = uuid.uuid4()
#             api_hit_count.time_refreshed = timezone.now()
#             api_hit_count.save()

#         # Increment the api_hits count
#         api_hit_count.api_hits += 1
#         api_hit_count.save()

#         serializer = self.get_serializer(api_hit_count)
#         return Response(serializer.data)