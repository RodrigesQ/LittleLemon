from django.test import TestCase
from django.urls import reverse
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of the Menu model
        MenuItem.objects.create(id="1", title="Burger", price=10.99, inventory="100")
        MenuItem.objects.create(id="2", title="Pizza", price=15.99, inventory="100")

    def test_getall(self):
        # Initialize REST framework's test client
        client = APIClient()

        # Retrieve all Menu objects via API
        url = reverse('menu-items')  # Assuming the URL name is 'menu/items/'
        response = client.get(url)

        # Serialize retrieved Menu objects
        menus = MenuItem.objects.all()
        serializer = MenuItemSerializer(menus, many=True)

        # Check if the serialized data equals the response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
