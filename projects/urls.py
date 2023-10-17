from rest_framework import routers
from django.urls import path, include
from projects.views import (
    ProfileViewSet,
    ProjectViewSet,
    CertificateViewSet,
    CertifyingInstitutionViewSet,
)

rotas = routers.DefaultRouter()

rotas.register(r"profiles", ProfileViewSet)
rotas.register(r"profiles/<int: id>", ProfileViewSet)
rotas.register(r"projects", ProjectViewSet)
rotas.register(r"projects/<int:id>", ProjectViewSet)
rotas.register(r"certifying-institutions", CertifyingInstitutionViewSet)
rotas.register(r"certificates", CertificateViewSet)

urlpatterns = [
    path("", include(rotas.urls)),
]
