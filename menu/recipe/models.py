from django.db import models

from django.contrib.auth.models import User
CATEGORY_CHOICES = [
    ('Indian', 'Indian'),
    ('Italian', 'Italian'),
    ('Fast Food', 'Fast Food'),
    ('Dessert', 'Dessert'),
    ('Salad', 'Salad'),
    ('Mandi', 'Mandi'),
    ('Drinks', 'Drinks'),
]

class Recipe(models.Model):


    owner = models.ForeignKey(User, on_delete=models.CASCADE
                              
)


    category = models.CharField(
    max_length=20,
    choices=CATEGORY_CHOICES,
    default='Indian'
)

 
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()

    image = models.ImageField(
        upload_to='recipes/',
        blank=True,
        null=True
     )

    def __str__(self):
        return self.title