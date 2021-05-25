from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LocateSerializer
from .models import Locate
from django.shortcuts import render


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/list/',
        'Create': '/create/'
    }
    return Response(api_urls)


@api_view(['GET'])
def locateList(request):
    locate = Locate.objects.all()
    serializer = LocateSerializer(locate, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def locateCreate(request):
    serializer = LocateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
