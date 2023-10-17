from django.apps import AppConfig

apc = AppConfig


class ProjectsConfig(apc):
    default_auto_field = "django.db.models.BigAutoField"
    name = "projects"
