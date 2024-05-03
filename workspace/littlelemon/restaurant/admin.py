from django.contrib import admin
from .models import MenuItem, Booking
from rest_framework.authtoken.models import Token

# Register your models here.
admin.site.register(MenuItem)
admin.site.register(Booking)
