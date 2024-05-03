from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        # Create a MenuItem object
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)

        # Check if the object was created successfully
        self.assertEqual(item.title, "IceCream")
        self.assertEqual(item.price, 80)
        self.assertEqual(item.inventory, 100)
