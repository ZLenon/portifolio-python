from django.db import models
from django.core.validators import MaxLengthValidator as mlgv, URLValidator


dj_model = models.Model


class Profile(dj_model):
    name = models.CharField(max_length=500)
    github = models.URLField(max_length=500)
    linkedin = models.URLField(max_length=500)
    bio = models.TextField(
        validators=[mlgv(limit_value=500)],
    )

    def __str__(self):
        return self.name


class Project(dj_model):
    name = models.CharField(max_length=500)
    keyword = models.CharField(max_length=500)
    github_url = models.URLField(max_length=500)
    key_skill = models.CharField(max_length=500)
    description = models.TextField(max_length=500)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CertifyingInstitution(dj_model):
    name = models.CharField(max_length=500, validators=[mlgv(limit_value=90)])
    url = models.URLField(validators=[URLValidator()])

    def __str__(self):
        return self.name


class Certificate(dj_model):
    name = models.CharField(max_length=500, validators=[mlgv(limit_value=90)])
    profiles = models.ManyToManyField("Profile", related_name="certificates")
    timestamp = models.DateTimeField(auto_now_add=True)
    certifying_institution = models.ForeignKey(
        CertifyingInstitution,
        on_delete=models.CASCADE,
        related_name="certificates",
    )

    def __str__(self):
        return self.name
