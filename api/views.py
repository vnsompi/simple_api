from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from api.serializers import ItemSerializer
from . models import Item
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def index(request):
    return Response({"message": "Welcome to the API index."})



@api_view(['POST'])
def index_post(request ):
    return Response({"message": "Welcome to the API index which is returning a POST response."})

# pour lister les items
@api_view(['GET'])
def get_all_item(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


# cette fonoction permet de cree 

@api_view(['POST'])
def create_item(request):
    serializer = ItemSerializer(data=request.data)  # DRF gère déjà le parsing
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


# une fonction qui va delete les Items 

@api_view(['PUT', 'DELETE'])
def update_or_delete_item(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=404)

    if request.method == 'PUT':
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response("deleted successfully",status=204)

