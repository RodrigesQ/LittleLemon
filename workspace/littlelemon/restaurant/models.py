from django.db import models

# Create your models here.
class Menu(models.Model):
    id = models.CharField(primary_key=True, max_length=5)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    id = models.CharField(primary_key=True, max_length=11)
    name = models.CharField(max_length=255)
    no_of_guests = models.CharField(max_length=6)
    bookingdate = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.name} on {self.bookingdate}"