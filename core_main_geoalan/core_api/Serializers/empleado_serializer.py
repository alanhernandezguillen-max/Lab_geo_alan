from admin_geoalan.models import Empleado
from rest_framework import serializers

# Serializers define the API representation.
class EmpleadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Empleado
        fields = ['nombre_completo', 'puesto', 'fecha_registro']