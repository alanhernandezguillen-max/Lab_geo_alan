from django.contrib import admin
from .models import Empleado, Direcciones

# Register your models here.
admin.site.register(Empleado)
admin.site.register(Direcciones)