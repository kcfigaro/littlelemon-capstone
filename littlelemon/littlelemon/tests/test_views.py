from django.test import TestCase
from restaurant.models import Menu

class MenuItemsViewTest(TestCase):
    def test_getall(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.title, "IceCream")
        self.assertEqual(item.price, 80)
