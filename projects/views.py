from rest_framework import viewsets
from projects.models import Profile, Project
from projects.serializers import ProfileSerializer, ProjectSerializer

set_view = viewsets.ModelViewSet


class ProfileViewSet(set_view):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProjectViewSet(set_view):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
