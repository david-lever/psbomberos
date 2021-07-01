from rest_framework import serializers
from appweb.models import Postulante


class PostulanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulante
        fields = ['rut', 'dv', 'pnombre', 'snombre', 'appaterno', 'apmaterno', 'edad', 'nivel']