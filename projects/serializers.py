from rest_framework import serializers
from projects.models import (
    Profile,
    Project,
    Certificate,
    CertifyingInstitution,
)

srms = serializers.ModelSerializer


class ProfileSerializer(srms):
    class Meta:
        model = Profile
        fields = ["id", "name", "github", "linkedin", "bio"]


class ProjectSerializer(srms):
    class Meta:
        model = Project
        fields = "__all__"


class CertificateSerializer(srms):
    class Meta:
        model = Certificate
        fields = "__all__"


class NestedCertificatesSerializer(srms):
    class Meta:
        model = Certificate
        fields = ["id", "name", "timestamp"]


class CertifyingInstitutionSerializer(srms):
    certificates = NestedCertificatesSerializer(many=True)

    class Meta:
        model = CertifyingInstitution
        fields = ["id", "name", "url", "certificates"]

    def create(self, validated_data):
        certificates_data = validated_data.pop("certificates")
        new_certifying_institution = CertifyingInstitution.objects.create(
            **validated_data
        )
        new_certificate = {}
        for certificate in certificates_data:
            new_certificate = {
                "name": certificate["name"],
                "certifying_institution": new_certifying_institution,
                "profiles": [],
            }
            CertificateSerializer().create(new_certificate)
        return new_certifying_institution
