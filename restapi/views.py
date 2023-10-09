from django.shortcuts import render
from rest_framework import viewsets
from .models import Task, User
from .serializer import TaskSerializer, UserSerializer


# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
