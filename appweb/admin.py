from django.contrib import admin
from .models import Personal, Cargo, Compania, Comuna, Provincia, Region  

# Register your models here.


admin.site.register(Personal)
admin.site.register(Cargo)
admin.site.register(Compania)
admin.site.register(Comuna)
admin.site.register(Provincia)
admin.site.register(Region)
