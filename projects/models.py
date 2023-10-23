from django.core.validators import MaxLengthValidator as msv
from django.db import models

set_model = models.Model


class Profile(set_model):
    name = models.CharField(max_length=80)
    github = models.URLField()
    linkedin = models.URLField()
    bio = models.TextField(
        validators=[msv(limit_value=500)],
    )

    def __str__(self) -> str:
        return self.name


class Project(set_model):
    name = models.CharField(max_length=80)
    description = models.TextField(
        validators=[msv(limit_value=800)],
    )
    github_url = models.URLField()
    keyword = models.CharField(max_length=80)
    key_skill = models.CharField(max_length=80)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="projects"
    )

    def __str__(self):
        return self.name


class CertifyingInstitution(set_model):
    name = models.CharField(max_length=80)
    url = models.URLField()

    def __str__(self):
        return self.name


class Certificate(set_model):
    name = models.CharField(max_length=80)
    certifying_institution = models.ForeignKey(
        CertifyingInstitution,
        on_delete=models.CASCADE,
        related_name="certificates",
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    profiles = models.ManyToManyField(Profile, related_name="certificates")

    def __str__(self):
        return self.name
