from django.shortcuts import render, get_object_or_404
from .models import Shape
#import nessassary serializers
from .serializers import ShapeSerializer
#import rest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import default_storage
# Create your views here.


@api_view(['GET'])
def get_shapes(request):
    shapes = Shape.objects.all().order_by('-timestamp') #order by timestamp
    serializer = ShapeSerializer(shapes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_shape_id(request, id):
    shape = get_object_or_404(Shape, pk=id)
    serializer = ShapeSerializer(shape, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def create_shape(request):
    data = request.data
    #validate the shape and color
    valid_shapes = ['triangle', 'circle', 'square']
    valid_colors = ['red', 'blue', 'green', 'yellow']
    
    if data['shape'] not in valid_shapes:
        return Response("shape doesn't exists",status=status.HTTP_400_BAD_REQUEST)
    if data['color'] not in valid_colors:
        return Response("color doesn't exists",status=status.HTTP_400_BAD_REQUEST)
    
    #sample filename: circle_blue.png
    filename = f"{data['shape']}_{data['color']}.png"
    
    #check if the imagefile exists, onlu save shape if file exists
    if not default_storage.exists(f"shapes/{filename}"):
        return Response(f"Image {filename} not found", status=status.HTTP_400_BAD_REQUEST)
    
    shape = Shape.objects.create(
        name = data['name'],
        shape = data['shape'],
        color = data['color'],
        image = f"shapes/{filename}"
    )
    
    shape.save()
    serializer = ShapeSerializer(shape, many=False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PATCH'])
def edit_shape(request, id):
    shape = get_object_or_404(Shape, pk=id)
    # Get 'color' and 'shape' from request data, default to current values if not provided
    #This way, if a key is missing, it will return None instead of raising an error
    updated_color = request.data.get('color', shape.color)
    updated_shape = request.data.get('shape', shape.shape)
    # Update the 'image' field if either 'color' or 'shape' is provided in the request data
    if 'color' in request.data or 'shape' in request.data:
        filename = f'{updated_shape}_{updated_color}.png'
        shape.image.name = f'shapes/{filename}'
    serializer = ShapeSerializer(shape, data=request.data, partial=True) #allowing partial updates
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_shape(request, id):
    try:
        shape = Shape.objects.get(pk=id)
        shape.delete()
        serializer = ShapeSerializer(shape, many=False)
        return Response(f"Shape deleted: {serializer.data}", status=status.HTTP_200_OK)
    except Shape.DoesNotExist:
        return Response(f"Shape id {id} is not found", status=status.HTTP_400_BAD_REQUEST)
