from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, serializers

from healthapp.serializer import DataSerializer

from .models import Data

# Create your views here.
@api_view(['GET'])
def getData(request):
    if request.query_params:
        my_data = Data.objects.filter(**request.query_params.dict())
    else:
        my_data = Data.objects.all()
        
    if my_data:
        serialized = DataSerializer(my_data, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def postData(request):
    serialized_data = DataSerializer(data=request.data)
    if Data.objects.filter(**request.data).exists():
        raise serializers.ValidationError("The data is already in the database")
    
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    else:
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def updateData(request, pk):
    get_data = Data.objects.get(pk=pk)
    serialized_data = DataSerializer(instance=get_data, data=request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    else:
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['DELETE'])
def deleteData(request, pk):
    get_data = get_object_or_404(Data, pk=pk)
    get_data.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)