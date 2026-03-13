from django.db import models
from django.contrib.auth.models import User
# We need to import the Item model you just created!
from items.models import Item 

class Message(models.Model):
    # Foreign Keys linking to Users and Items as per ER Diagram
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='messages')
    
    # Message content and timestamp
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.receiver.username}"