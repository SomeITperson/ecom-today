from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from todo.models import *
from rest_framework.response import Response
from todo.serializers import *
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from .service import *


"""Создание записи"""
class TodoCreateAPIView(APIView):
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"status": status.HTTP_201_CREATED, "created": True})

"""Удаление записи по uuid"""
class TodoRemoveAPIView(generics.DestroyAPIView):
    serializer_class = TodoSerializer
    lookup_field = 'uuid'
    
    def get_queryset(self):
        param = self.kwargs.get('uuid')
        return Todo.objects.filter(uuid=param)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

"""Получение всех записей"""
class TodoGetAPIView(APIView):
    def get(self, request):
        todo = Todo.objects.all()
        return Response({"todo": TodoSerializer(todo, many=True).data})


"""Фильтрация по uuid"""
class TodoGetByUUID(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['uuid']


"""Фильтрация по дате создания"""
class TodoGetByDate(generics.ListAPIView):
    filter_class = TodoFilter
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        start = self.request.query_params.get('start',None)
        end = self.request.query_params.get('end',None)
        response  = Todo.objects.filter(created__gte=start, created__lte=end)
        return response