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
        data = validated_data.pop("certificates")
        novo_certificado = CertifyingInstitution.objects.create(
            **validated_data
        )
        certificado = {}
        for x in data:
            certificado = {
                "name": x["name"],
                "certifying_institution": novo_certificado,
                "profiles": [],
            }
            CertificateSerializer().create(certificado)
        return novo_certificado
