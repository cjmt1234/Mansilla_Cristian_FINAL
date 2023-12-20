from rest_framework import serializers
from EvaFinalApp import models

class InscritosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Inscritos
        fields = '__all__'

class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Institucion
        fields = '__all__'