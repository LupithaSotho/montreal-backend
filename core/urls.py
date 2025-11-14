from rest_framework.routers import DefaultRouter
from .views import CursoViewSet, InscripcionViewSet, CertificacionViewSet

router = DefaultRouter()
router.register("cursos", CursoViewSet)
router.register("inscripciones", InscripcionViewSet)
router.register("certificaciones", CertificacionViewSet)

urlpatterns = router.urls
