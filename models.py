from django.db import models
from django.contrib.auth.models import User

class Pizza(models.Model):
    SIZE_CHOICES = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ]

    CRUST_CHOICES = [
        ('normal', 'Normal'),
        ('thin', 'Thin'),
        ('thick', 'Thick'),
        ('gluten_free', 'Gluten Free'),
    ]

    SAUCE_CHOICES = [
        ('tomato', 'Tomato'),
        ('bbq', 'BBQ'),
    ]

    CHEESE_CHOICES = [
        ('mozzarella', 'Mozzarella'),
        ('vegan', 'Vegan'),
        ('low_fat', 'Low Fat'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    crust = models.CharField(max_length=20, choices=CRUST_CHOICES)
    sauce = models.CharField(max_length=20, choices=SAUCE_CHOICES)
    cheese = models.CharField(max_length=20, choices=CHEESE_CHOICES)

    pepperoni = models.BooleanField(default=False)
    chicken = models.BooleanField(default=False)
    ham = models.BooleanField(default=False)
    pineapple = models.BooleanField(default=False)
    peppers = models.BooleanField(default=False)
    mushrooms = models.BooleanField(default=False)
    onions = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s {self.size} pizza"
    
class DeliveryDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    card_number = models.CharField(max_length=50)
    card_expiry_date = models.CharField(max_length=10)
    card_cvv = models.CharField(max_length=3, default='000')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Delivery for {self.name} ({self.address})"
