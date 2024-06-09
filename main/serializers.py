#to convert model into json compatible data
from rest_framework import serializers
from .models import Shape

class ShapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shape;
        fields = '__all__'