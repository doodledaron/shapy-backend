#to convert model into json compatible data
from rest_framework import serializers
from main.models import Shape

class ShapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shape;
        fields = ['name', 'timestamp', 'image']