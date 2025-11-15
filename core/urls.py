from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CursoViewSet, InscripcionViewSet, CertificacionViewSet

router = DefaultRouter()
router.register(r"cursos", CursoViewSet)
router.register(r"inscripciones", InscripcionViewSet)
router.register(r"certificaciones", CertificacionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
