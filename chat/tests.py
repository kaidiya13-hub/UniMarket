from django.test import TestCase
from django.contrib.auth.models import User
from items.models import Item
from .models import Message

class MessageModelTest(TestCase):

    def setUp(self):
        self.sender = User.objects.create(username="user1")
        self.receiver = User.objects.create(username="user2")

        self.item = Item.objects.create(
            seller=self.receiver,
            title="Test Item",
            description="Test description",
            price=20,
            category="Electronics",
            condition="Good"
        )

    def test_message_creation(self):
        message = Message.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            item=self.item,
            content="Hello"
        )

        self.assertEqual(message.content, "Hello")