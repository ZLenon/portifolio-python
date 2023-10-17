from rest_framework import serializers
from projects.models import Profile, Project

srms = serializers.ModelSerializer


class ProfileSerializer(srms):
    class Meta:
        model = Profile
        fields = ("id", "name", "github", "linkedin", "bio")


class ProjectSerializer(srms):
    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "description",
            "github_url",
            "keyword",
            "key_skill",
            "profile",
        )
