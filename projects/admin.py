from django.contrib import admin as adm
from projects.models import (
    Profile,
    Project,
    Certificate,
    CertifyingInstitution,
)

adm_site = adm.site


class CertificateInline(adm.StackedInline):
    model = Certificate


class CertifyingInstitutionAdmin(adm.ModelAdmin):
    inlines = [CertificateInline]


adm_site.register(Profile)
adm_site.register(Project)
adm_site.register(CertifyingInstitution, CertifyingInstitutionAdmin)
adm_site.register(Certificate)
