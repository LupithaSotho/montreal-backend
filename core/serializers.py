from rest_framework import serializers
from .models import Curso, Inscripcion, Certificacion


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"


class InscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscripcion
        fields = "__all__"


class CertificacionSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
=======
    # Para que el frontend pueda usar c.curso_nombre
>>>>>>> a77a73ddba28b1b60b4ed6555f873c74ffe13654
    curso_nombre = serializers.CharField(source="curso.nombre", read_only=True)

    class Meta:
        model = Certificacion
        fields = ["id", "alumno", "curso", "curso_nombre", "folio", "fecha_emision"]
