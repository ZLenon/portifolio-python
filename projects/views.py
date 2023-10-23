from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import (
    Profile,
    Project,
    Certificate,
    CertifyingInstitution,
)
from .serializers import (
    ProfileSerializer,
    ProjectSerializer,
    CertificateSerializer,
    CertifyingInstitutionSerializer,
)


set_view = viewsets.ModelViewSet


class ProfileViewSet(set_view):
    # defina a queryset
    queryset = Profile.objects.all()
    # defina a classe do serializer
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        if self.request.method != "GET":
            return super().retrieve(request, *args, **kwargs)
        else:
            # busque o id do perfil
            kwargs.get("pk")
            # crie uma variável para guardar esse perfil
            x = self.get_object()
            return render(
                # passe os parâmetros necessários para o template:
                request,
                # a requisição, o caminho do template
                "profile_detail.html",
                {"profile": x},
                # e um dict com dados para o template
            )


class ProjectViewSet(set_view):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CertifyingInstitutionViewSet(set_view):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer


class CertificateViewSet(set_view):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
