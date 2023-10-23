from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from projects.models import (
    Profile,
    Project,
    Certificate,
    CertifyingInstitution,
)
from projects.serializers import (
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
            path = request.META["PATH_INFO"]
            user_id = int(path.split("/")[2])
            # crie uma variável para guardar esse perfil
            profile = get_object_or_404(Profile, id=user_id)
            context = {
                "profile": profile,
                "certificates": profile.certificates.all(),
                "projects": profile.projects.all(),
            }
            return render(
                # passe os parâmetros necessários para o template:
                request,
                # a requisição, o caminho do template
                "profile_detail.html",
                context
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
