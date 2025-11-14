<<<<<<< HEAD
=======
from django.urls import path, include
>>>>>>> a77a73ddba28b1b60b4ed6555f873c74ffe13654
from rest_framework.routers import DefaultRouter
from .views import CursoViewSet, InscripcionViewSet, CertificacionViewSet

router = DefaultRouter()
<<<<<<< HEAD
router.register("cursos", CursoViewSet)
router.register("inscripciones", InscripcionViewSet)
router.register("certificaciones", CertificacionViewSet)

urlpatterns = router.urls
=======
router.register(r"cursos", CursoViewSet)
router.register(r"inscripciones", InscripcionViewSet)
router.register(r"certificaciones", CertificacionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
>>>>>>> a77a73ddba28b1b60b4ed6555f873c74ffe13654
