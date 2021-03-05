from django.shortcuts import render

from rest_framework import viewsets
from .serializers import VideoSerializer
from .models import Videos

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Videos.objects.all()
    serializer_class = VideoSerializer
