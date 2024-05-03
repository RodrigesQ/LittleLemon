# views.py
from rest_framework.decorators import api_view
from rest_framework import viewsets, generics, permissions
#from rest_framework.permissions import IsAuthenticated
#from rest_framework import generics
from django.shortcuts import render
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

