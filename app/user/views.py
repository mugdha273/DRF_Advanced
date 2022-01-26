from django.shortcuts import render
from itsdangerous import serializer
from rest_framework import generics
from . import UserSerializer
# Create your views here.

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer