# hackathon/urls.py

from django.urls import path
from .views import TeamRegistrationView, TeamInfoView

urlpatterns = [
    path('register/', TeamRegistrationView.as_view(), name='team-registration'),
    path('team-info/', TeamInfoView.as_view(), name='team-info'),
    # path('api-code/', ApiCodeView.as_view(), name='api-code'),

]
