from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render

from django.contrib.auth.models import User
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer, UserSerializer
# Create your views here.


class BookingView(APIView): 
    def get(self, request): 
        items = Booking.objects.all()
        serialized_items = BookingSerializer(items, many=True)
        return Response(serialized_items.data, status.HTTP_200_OK)
    
    def post(self, request): 
        serialized_data = BookingSerializer(data=request.data)

        if serialized_data.is_valid(): 
            serialized_data.save()
            return Response({"status":"success", "data":serialized_data.data}, status.HTTP_200_OK)
        else : 
            return Response(serialized_data.errors, status.HTTP_400_BAD_REQUEST)
 

class MenuView(APIView): 
    def get(self, request): 
        items = Menu.objects.all()
        serialized_items = MenuSerializer(items, many=True)
        return Response(serialized_items.data, status.HTTP_200_OK)
    
    def post(self, request): 
        serialized_data = MenuSerializer(data=request.data)

        if serialized_data.is_valid(): 
            serialized_data.save()
            return Response({"status":"success", "data":serialized_data.data}, status.HTTP_200_OK)
        else : 
            return Response(serialized_data.errors, status.HTTP_400_BAD_REQUEST)
        

class UserView(APIView): 
    def get(self, request): 
        items = User.objects.all()
        serialized_items = UserSerializer(items, many=True)
        return Response(serialized_items.data, status.HTTP_200_OK)
    

class MenuItemsView(generics.ListCreateAPIView): 
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemsView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView): 
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
     



 
