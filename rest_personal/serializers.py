from rest_framework import serializers
from appweb.models import Personal

class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = ['rut', 'dv', 'pnombre', 'snombre', 'appaterno', 'apmaterno','cargo', 'fono','comuna','fecha_ing']
