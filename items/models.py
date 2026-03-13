from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    # Choices for dropdown menus in the UI (based on wireframes)
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Sold', 'Sold'),
    ]
    CONDITION_CHOICES = [
        ('New', 'New'),
        ('Like New', 'Like New'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
    ]
    CATEGORY_CHOICES = [
        ('Textbooks', 'Textbooks'),
        ('Electronics', 'Electronics'),
        ('Furniture', 'Furniture'),
        ('Other', 'Other'),
    ]

    # Maps to user_id {FK} in the ER diagram. If a user is deleted, their items are also deleted.
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items') 
    
    # Core item details
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2) 
    
    # Image field (requires Pillow library to be installed)
    image = models.ImageField(upload_to='item_images/', blank=True, null=True) 
    
    # Categorization and status
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    condition = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    
    # Tracks availability ('Active' or 'Sold') as per Data Dictionary
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
    
    # Automatically records the timestamp when the item is created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title