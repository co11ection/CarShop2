from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from . import serializers
from .models import Category
# Create your views here.


class Category(ModelViewSet):
    queryset = Category.objects.all()
    

