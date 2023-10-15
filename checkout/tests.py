from django.test import TestCase
from .models import Order, OrderLineItem, UserPurchase

class OrderModelTest(TestCase):

    def test_order_creation(self):
        order = Order.objects.create(
            full_name="John Doe",
            email="john@example.com",
            phone_number="1234567890",
            country="US",
            town_or_city="New York",
            street_address1="123 Main St",
            # Add other required fields
        )
        self.assertEqual(order.full_name, "John Doe")
