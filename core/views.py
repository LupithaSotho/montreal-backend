from rest_framework import viewsets
from .models import Curso, Inscripcion, Certificacion
from .serializers import CursoSerializer, InscripcionSerializer, CertificacionSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all().order_by("nombre")
    serializer_class = CursoSerializer


class InscripcionViewSet(viewsets.ModelViewSet):
    queryset = Inscripcion.objects.all().order_by("-creado_en")
    serializer_class = InscripcionSerializer


class CertificacionViewSet(viewsets.ModelViewSet):
    queryset = Certificacion.objects.all().order_by("-fecha_emision")
    serializer_class = CertificacionSerializer
