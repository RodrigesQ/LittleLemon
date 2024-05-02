# serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu, Booking

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'  # Use '__all__' to include all fields from the model
'''
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
'''

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'