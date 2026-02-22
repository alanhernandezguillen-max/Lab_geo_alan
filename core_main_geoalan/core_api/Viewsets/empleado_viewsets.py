from core_api.Serializers.empleado_serializer import *
from rest_framework import viewsets

# ViewSets define the view behavior.
class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer