from django.shortcuts import render

from rest_framework import viewsets
from .models import Task, Tag
from .serializers import TaskSerializer, TagSerializer

# Create your views here.
class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()    
    serializer_class = TagSerializer