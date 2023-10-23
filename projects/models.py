from django.db import models
from django.core.validators import MaxLengthValidator as mlgv, URLValidator


dj_model = models.Model


class Profile(dj_model):
    name = models.CharField(max_length=60)
    github = models.URLField()
    linkedin = models.URLField()
    bio = models.TextField(
        validators=[mlgv(limit_value=500)],
    )

    def __str__(self):
        return self.name


class Project(dj_model):
    name = models.CharField(max_length=60)
    keyword = models.CharField(max_length=60)
    github_url = models.URLField()
    key_skill = models.CharField(max_length=60)
    description = models.TextField(max_length=500)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CertifyingInstitution(dj_model):
    name = models.CharField(max_length=60, validators=[mlgv(limit_value=90)])
    url = models.URLField(validators=[URLValidator()])

    def __str__(self):
        return self.name


class Certificate(dj_model):
    name = models.CharField(max_length=60, validators=[mlgv(limit_value=90)])
    profiles = models.ManyToManyField(Profile, related_name="certificates")
    timestamp = models.DateTimeField(auto_now_add=True)
    certifying_institution = models.ForeignKey(
        CertifyingInstitution,
        on_delete=models.CASCADE,
        related_name="certificates",
    )

    def __str__(self):
        return self.name
