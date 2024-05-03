# serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import MenuItem, Booking, MenuItem

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']  # Define fields to be serialized
