from django.test import TestCase
from django.contrib.auth.models import User
from .models import Item

class ItemModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="seller")

    def test_active_item_creation(self):
        item = Item.objects.create(
            seller=self.user,
            title="Test Item",
            description="Test description",
            price=10.00,
            category="Electronics",
            condition="Good",
            status="Active"
        )

        self.assertEqual(item.status, "Active")