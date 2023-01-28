from rest_framework import serializers
from api.models import Estudiante, RolUic

class EstudianteSerializer (serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = "__all__"
        
class RolUicSerializer (serializers.ModelSerializer):
    class Meta:
        model = RolUic
        fields = "__all__" 