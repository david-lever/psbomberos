from django.contrib import admin
from .models import Cargo, Comuna, Personal, NivelAcademico, Postulante

# Register your models here.

admin.site.register(Cargo)
admin.site.register(Comuna)
admin.site.register(Personal)
admin.site.register(NivelAcademico)
admin.site.register(Postulante)