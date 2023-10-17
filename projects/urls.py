from rest_framework import routers
from django.urls import path, include
from projects.views import ProfileViewSet, ProjectViewSet

rotas = routers.DefaultRouter()
rotas.register("profiles/<int: id>", ProfileViewSet)
rotas.register(r"profiles", ProfileViewSet)
rotas.register(r"projects", ProjectViewSet)

urlpatterns = [
    path("", include(rotas.urls)),
]
