from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

from django.contrib.auth.models import User
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer, UserSerializer

def home(request): 
    return render(request, 'index.html')
        
class UserView(APIView): 
    def get(self, request): 
        items = User.objects.all()
        serialized_items = UserSerializer(items, many=True)
        return Response(serialized_items.data, status.HTTP_200_OK)
    

class MenuItemsView(generics.ListCreateAPIView): 
    permission_classes=[IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemsView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView): 
    permission_classes=[IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer





 
