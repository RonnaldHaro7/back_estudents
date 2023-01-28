from rest_framework.routers import DefaultRouter
from api.views import EstudianteViewSet, RolUicViewSet

router = DefaultRouter()

router.register('api/estudiante', EstudianteViewSet)
router.register('api/rolUic', RolUicViewSet)

urlpatterns = []

urlpatterns +=router.urls
