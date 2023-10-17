from django.db import models
from django.core.validators import MaxLengthValidator as mlgv


dj_model = models.Model


class Profile(dj_model):
    name = models.CharField(max_length=100)
    github = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)
    bio = models.TextField(
        validators=[mlgv(limit_value=500)],
    )

    def __str__(self):
        return self.name


class Project(dj_model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    github_url = models.URLField(max_length=200)
    keyword = models.CharField(max_length=100)
    key_skill = models.CharField(max_length=100)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="projects"
    )

    def __str__(self):
        return self.name
