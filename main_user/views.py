from main.models import Shape
from .serializers import ShapeSerializer
#import rest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def get_shapes(request):
    shapes = Shape.objects.all().order_by('-timestamp') #order by timestamp
    serializer = ShapeSerializer(shapes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
