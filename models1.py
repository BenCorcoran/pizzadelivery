from django.db import models

class Game(models.Model):
    PLATFORM_CHOICES = [
        ('PS5', 'PlayStation 5'),
        ('XBOX', 'Xbox One'),
        ('SWITCH', 'Nintendo Switch'),
        ('PC', 'PC'),
    ]

    GENRE_CHOICES = [
        ('SHOOTER', 'Shooter'),
        ('ACTION', 'Action'),
        ('ADVENTURE', 'Adventure'),
        ('RPG', 'Role-Playing Game'),
        ('SPORTS', 'Sports'),
        ('STRATEGY', 'Strategy'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    platform = models.CharField(max_length=10, choices=PLATFORM_CHOICES)
    genre = models.CharField(max_length=15, choices=GENRE_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.platform})"
