from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import CursoViewSet, InscripcionViewSet, CertificacionViewSet
# ajusta "core" al nombre real de tu app

router = DefaultRouter()
router.register(r"cursos", CursoViewSet, basename="curso")
router.register(r"inscripciones", InscripcionViewSet, basename="inscripcion")
router.register(r"certificaciones", CertificacionViewSet, basename="certificacion")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
