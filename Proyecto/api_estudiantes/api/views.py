from rest_framework import viewsets

from api.models import Estudiante, RolUic
from api.serializers import EstudianteSerializer, RolUicSerializer

class EstudianteViewSet (viewsets.ModelViewSet):
    serializer_class = EstudianteSerializer
    queryset = Estudiante.objects.all()
    
class RolUicViewSet (viewsets.ModelViewSet):
    serializer_class = RolUicSerializer
    queryset = RolUic.objects.all()
